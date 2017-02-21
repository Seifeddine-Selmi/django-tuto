#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from datetime import datetime
from blog.models import Article, Contact, Document, Category
from .forms import ContactForm, ArticleForm, NewContactForm, NewDocumentForm
from django.core.mail import send_mail, BadHeaderError
from django.views.generic import TemplateView, ListView, DetailView


def index(request):

    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/index.html', {'articles': articles})


def view_article(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/view_article.html', {'article': article})


def add_article(request):
    form = ArticleForm(request.POST or None)
    save = False
    if form.is_valid():
        form.save()
        save = True
        return HttpResponseRedirect('/blog/')

    return render(request, 'blog/add_article.html',{
        'form': form,
        'save': save
    })


def edit_article(request, id):
    article = get_object_or_404(Article, pk=id)
    #article = Article.objects.get(pk=id)

    form = ArticleForm(
        data=request.POST or None,
        files=request.FILES or None,
        instance=article
    )
    if form.is_valid():
        form.save()
        save = True
        return HttpResponseRedirect('/blog/')

    return render(request, 'blog/edit_article.html', locals())


def delete_article(request, id):
    get_object_or_404(Article, pk=id).delete()
    return HttpResponseRedirect('/blog/')


def new_contact(request):
    save = False
    form = NewContactForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        contact = Contact()
        contact.name = form.cleaned_data["name"]
        contact.address = form.cleaned_data["address"]
        contact.image = form.cleaned_data["image"]
        contact.save()
        save = True

    return render(request, 'blog/new_contact.html', {
        'form': form,
        'save': save
    })


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'blog/contact_list.html', {'contacts': contacts})


def new_document(request):
    save = False
    form = NewDocumentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        document = Document()
        document.name = form.cleaned_data["name"]
        document.file = form.cleaned_data["file"]
        document.save()
        save = True

    return render(request, 'blog/new_document.html', {
        'form': form,
        'save': save
    })


def document_list(request):
    documents = Document.objects.all()
    return render(request, 'blog/document_list.html', {'documents': documents})


def contact(request):

    form = ContactForm(request.POST or None)
    if form.is_valid():

        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['from_email']
        resend = form.cleaned_data['resend']

        send = True
        if subject and message and from_email:
           try:
                send_mail(subject, message, from_email, ['selmi.seifeddine19@gmail.com'])
           except BadHeaderError:
               return HttpResponse('Invalid header found.')
           return HttpResponseRedirect('/blog/contact/')

    return render(request, 'blog/contact.html', locals())


def faq(request):
    return render(request, 'blog/faq.html', {})


### Views generic ###


class FAQView(TemplateView):
    template_name = "blog/faq.html"


class ListArticles(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "blog/article_list.html"
    paginate_by = 5
    #queryset = Article.objects.order_by('-date')

    def get_queryset(self):

        return Article.objects.order_by('-date')

    def get_context_data(self, **kwargs):
        # Nous récupérons le contexte depuis la super-classe
        context = super(ListArticles, self).get_context_data(**kwargs)

        context['categories'] = Category.objects.all()
        return context


class ListArticlesByCategory(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "blog/article_list.html"
    paginate_by = 5
    #queryset = Article.objects.filter(category__id=1)

    def get_queryset(self):
        return Article.objects.filter(category__id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        # Nous récupérons le contexte depuis la super-classe
        context = super(ListArticlesByCategory, self).get_context_data(**kwargs)

        context['categories'] = Category.objects.all()
        return context


class DetailArticle(DetailView):
    context_object_name = "article"
    model = Article
    template_name = "blog/view_article.html"

    def get_object(self):
        # Nous récupérons l'objet, via la super-classe
        article = super(DetailArticle, self).get_object()

        #article.nb_views += 1  # Imaginons un attribut « Nombre de vues »
       # article.save()

        return article  # Et nous retournons l'objet à afficher
