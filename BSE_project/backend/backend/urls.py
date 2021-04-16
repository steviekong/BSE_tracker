from django.contrib import admin
from django.urls import path
import requests
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search', views.search_by_name, name='search'),
]
