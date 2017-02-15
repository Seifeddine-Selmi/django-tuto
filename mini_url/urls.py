#-*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    # Une string vide indique la racine
    url(r'^$', views.url_list, name='url_list'),
    url(r'^new_url$', views.new_url, name='new_url'),
    # (?P<code>\w{6}) capturera 6 caractères alphanumériques. 
    url(r'^(?P<code>\w{6})/$', views.url_redirection, name='url_redirection'),
]