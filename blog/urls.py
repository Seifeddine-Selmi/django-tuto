from django.conf.urls import url
from django.views.generic import TemplateView, ListView
from . import views
from .models import Article

urlpatterns = [
    #url(r'^$', views.index, name='index'),

    #url(r'^article/(?P<id>\d+)$', views.view_article, name="view_article"),
    url(r'^add_article/$', views.add_article, name='add_article'),
    url(r'^edit_article/(?P<id>\d+)$', views.edit_article, name='edit_article'),
    url(r'^delete_article/(?P<id>\d+)$', views.delete_article, name='delete_article'),

    url(r'^new_contact/$', views.new_contact, name='new_contact'),
    url(r'^contact_list/$', views.contact_list, name='contact_list'),

    url(r'^new_document/$', views.new_document, name='new_document'),
    url(r'^document_list/$', views.document_list, name='document_list'),

    url(r'^contact/$', views.contact, name='contact'),

    ### Views generic ###
    #url('faq', views.faq, name='faq'),
    #url(r'^faq$', views.FAQView.as_view()),
    url(r'^faq', TemplateView.as_view(template_name='blog/faq.html')),


    #url(r'^$', ListView.as_view(model=Article,)), # call blog/article_list.html
    #url(r'^$', ListView.as_view(model=Article, context_object_name="articles", template_name="blog/article_list.html")),
    url(r'^$', views.ListArticles.as_view(), name="blog_list"),
    url(r'^category/(?P<id>\d+)', views.ListArticlesByCategory.as_view(), name="blog_category"),
    url(r'^article/(?P<pk>\d+)$', views.DetailArticle.as_view(), name='blog_article'),

]