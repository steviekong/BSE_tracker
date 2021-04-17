from django.contrib import admin
from django.urls import path
import requests
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search_by_name, name='search'),
    path('download', views.download_results_csv, name='download_results_csv'),
]