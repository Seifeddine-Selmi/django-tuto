from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home', views.home),
    url(r'^article/(?P<id>\d+)$', views.view, name="view_article"),
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})$', views.list_articles),

    url(r'^redirection$', views.view_redirection),

    url(r'^date$', views.date_actuelle),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^add_article/$', views.add_article, name='add_article'),
    url(r'^edit_article/(?P<id>\d+)$', views.edit_article, name='edit_article'),
    url(r'^delete_article/(?P<id>\d+)$', views.delete_article, name='delete_article'),
    url(r'^new_contact/$', views.new_contact, name='new_contact'),
    url(r'^contact_list/$', views.contact_list, name='contact_list'),
    url(r'^new_document/$', views.new_document, name='new_document'),
    url(r'^document_list/$', views.document_list, name='document_list'),
]