# -*- coding: utf-8 -*-

from django.conf.urls import url

from books import views

app_name = 'books'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^Add$', views.AddView.as_view(), name='add'),
    url(r'^Save/$', views.Save, name='save'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
        
        



