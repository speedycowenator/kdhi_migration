
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
	path('rok-biographic/<str:name>', views.rok_individual_detail, name='rok_individual_detail'),
	path('rok-institution/<str:name>', views.rok_institution_detail, name='rok_institution_detail'),
	path('article/<str:slug>', views.article_detail, name='article_detail'),
	path('biographic', views.individual_list, name='individual_list'),
	path('institution', views.institution_list, name='institution_list'),	
	path('', views.homepage_view, name='homepage'),
	path('glossary/<str:slug>', views.glossary_detail, name='glossary_detail'),

]
