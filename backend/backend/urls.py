from django.contrib import admin
from django.urls import path, re_path
import requests
from . import views

urlpatterns = [
    path('api/search', views.search_by_name, name='search'),
    path('api/download', views.download_results_csv,
         name='download_results_csv'),
    re_path(r'^(?:.*)/?$', views.index),
]
