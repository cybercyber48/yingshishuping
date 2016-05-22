# -*- coding: utf-8 -*-

from django.conf.urls import url

from main import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.HomePageView, name='HomePageView'),
    url(r'^Search/$', views.Search, name='Search'),
    url(r'^SearchImage/$', views.SearchImage, name='SearchImage'),
]