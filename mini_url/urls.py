#-*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    # Une string vide indique la racine
    #url(r'^$', views.url_list, name='url_list'),
    #url(r'^new_url$', views.new_url, name='url_create'),
    # (?P<code>\w{6}) capturera 6 caractères alphanumériques. 
    url(r'^(?P<code>\w{6})/$', views.url_redirection, name='url_redirection'),

    ### Views generic  CRUD ###
    url(r'^$', views.ListUrl.as_view(), name='url_list'),
    url(r'^url$', views.URLCreate.as_view(), name='url_create'),
    #url(r'^edit/(?P<pk>\d+)$', views.URLUpdate.as_view(), name='url_update'),
    url(r'^edit/(?P<code>\w{6})$', views.URLUpdate.as_view(), name='url_update'),

    url(r'^delete/(?P<code>\w{6})$', views.URLDelete.as_view(), name='url_delete')
]