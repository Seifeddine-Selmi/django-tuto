#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from datetime import datetime
from blog.models import Article
from .forms import ContactForm, ArticleForm
from django.core.mail import send_mail, BadHeaderError

def index(request):


    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/index.html', {'articles': articles})


def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Bienvenue sur mon blog !</h1>"""
    return HttpResponse(text)

def view_article(request, id_article):
    """
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """

    if int(id_article) > 100:
        #raise Http404
        return redirect(view_redirection)
    return HttpResponse(
        "Vous avez demandé l'article #{0} !".format(id_article)
    )

def view_redirection(request):
    return HttpResponse("Article n'existe pas !!!.")

def view(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/view.html', {'article': article})



def list_articles(request, month, year):
    """ Liste des articles d'un mois précis. """

    #return redirect('view_article', id_article=42)
    return HttpResponse(
        "Vous avez demandé les articles de {0} {1}.".format(month, year)
    )

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):
    total = int(nombre1) + int(nombre2)

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())


def contact(request):

    form = ContactForm(request.POST or None)
    if form.is_valid():

        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['from_email']
        resend = form.cleaned_data['resend']

        #send = True
        if subject and message and from_email:
           try:
                send_mail(subject, message, from_email, ['selmi.seifeddine19@gmail.com'])
           except BadHeaderError:
               return HttpResponse('Invalid header found.')
           return HttpResponseRedirect('/blog/contact/')

    return render(request, 'blog/contact.html', locals())


def add_article(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/blog/')

    return render(request, 'blog/add.html', {'form': form})


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
        return HttpResponseRedirect('/blog/')

    return render(request, 'blog/edit.html', locals())