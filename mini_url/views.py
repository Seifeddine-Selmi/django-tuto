#-*- coding: utf-8 -*-
from django.shortcuts import redirect, get_object_or_404, render
from mini_url.models import MiniURL
from mini_url.forms import MiniURLForm
from pprint import pprint
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages


def url_list(request):
    """ Affichage des redirections """
    minis = MiniURL.objects.order_by('-nb_access')
    return render(request, 'mini_url/miniurl_list.html', locals())


def new_url(request):
    """ Ajout d'une redirection """
    if request.method == "POST":
        form = MiniURLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(url_list)
    else:
        form = MiniURLForm()

    return render(request, 'mini_url/new_url.html', {'form': form})


def url_redirection(request, code):
    """ Redirection vers l'URL enregistrée """

    #pprint(vars(code))
    mini = get_object_or_404(MiniURL, code=code)
    mini.nb_access += 1
    mini.save()

    return redirect(mini.url, permanent=True)

### Views generic  CRUD ###


class ListUrl(ListView):
    model = MiniURL
    context_object_name = "minis"
    template_name = "mini_url/miniurl_list.html"
    paginate_by = 5
    queryset = MiniURL.objects.order_by('-date')


class URLCreate(CreateView):
    model = MiniURL
    #template_name = 'mini_url/miniurl_form.html'
    form_class = MiniURLForm
    success_url = reverse_lazy('url_list')


class URLUpdate(UpdateView):
    model = MiniURL
    #template_name = 'mini_url/miniurl_form.html'
    form_class = MiniURLForm
    success_url = reverse_lazy('url_list')

    def get_object(self, queryset=None):
        code = self.kwargs.get('code', None)
        return get_object_or_404(MiniURL, code=code)

    def form_valid(self, form):
        self.object = form.save()
        # Envoi d'un message à l'utilisateur
        messages.success(self.request, "Votre url a été mis à jour avec succès.")
        return HttpResponseRedirect(self.get_success_url())


class URLDelete(DeleteView):
    model = MiniURL
    context_object_name = "mini_url"
    #template_name = 'mini_url/miniurl_confirm_delete.html'
    success_url = reverse_lazy('url_list')

    def get_object(self, queryset=None):
        code = self.kwargs.get('code', None)
        return get_object_or_404(MiniURL, code=code)


