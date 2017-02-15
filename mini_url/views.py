#-*- coding: utf-8 -*-
from django.shortcuts import redirect, get_object_or_404, render
from mini_url.models import MiniURL
from mini_url.forms import MiniURLForm
from pprint import pprint


def url_list(request):
    """ Affichage des redirections """
    minis = MiniURL.objects.order_by('-nb_access')
    return render(request, 'mini_url/url_list.html', locals())


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
