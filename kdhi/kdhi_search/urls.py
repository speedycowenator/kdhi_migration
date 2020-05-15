
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from . import views
from django.conf.urls import url
from main_site import views as core_views

urlpatterns = [
	path('', views.search_console, name='search_console'),
	]