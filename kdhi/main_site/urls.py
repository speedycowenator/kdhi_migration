
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from . import views
from django.conf.urls import url
from main_site import views as core_views

urlpatterns = [
    #url('', views.search_redirect, name='redirect'),
	path('biographic/<str:name>', views.individual_detail, name='individual_detail'),
	path('institution/<str:name>', views.institution_detail, name='institution_detail'),	
]
