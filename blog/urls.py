from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^article/(?P<id>\d+)$', views.view_article, name="view_article"),
    url(r'^add_article/$', views.add_article, name='add_article'),
    url(r'^edit_article/(?P<id>\d+)$', views.edit_article, name='edit_article'),
    url(r'^delete_article/(?P<id>\d+)$', views.delete_article, name='delete_article'),

    url(r'^new_contact/$', views.new_contact, name='new_contact'),
    url(r'^contact_list/$', views.contact_list, name='contact_list'),

    url(r'^new_document/$', views.new_document, name='new_document'),
    url(r'^document_list/$', views.document_list, name='document_list'),

    url(r'^contact/$', views.contact, name='contact'),

    url('faq', views.faq, name='faq'),
]