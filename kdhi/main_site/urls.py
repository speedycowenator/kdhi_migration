
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from . import views
from django.conf.urls import url
from main_site import views as core_views

urlpatterns = [
    #url('', views.search_redirect, name='redirect'),
	path('dpkr-biographic', views.individual_list, name='dprk_individual_list'),
	path('dpkr-biographic/<str:name>', views.individual_detail, name='individual_detail'),
	path('institution/<str:name>', views.institution_detail, name='institution_detail'),	
	path('dprk-institution', views.dprk_institution_landing, name='dprk_institution_landing'),	
	path('rok-biographic/<str:name_slug>', views.rok_individual_detail, name='rok_individual_detail'),
	path('rok-biographic', views.rok_individual_list, name='rok_individual_list'),
	path('rok-institution/<str:slug>', views.rok_institution_detail, name='rok_institution_detail'),
	path('rok-institution', views.rok_institution_landing, name='rok_institution_landing'),
	path('', views.homepage_view, name='homepage'),
	path('glossary', views.glossary_list, name='glossary_list'),
	path('glossary/<str:slug>', views.glossary_detail, name='glossary_detail'),
	path('about', views.about_page, name='about_page'),
	path('articles/<str:slug>', views.article_detail, name='article_detail'),
	path('articles', views.research_page, name='research_page'),
	path('inter-korean-spending/2018', views.inter_korean_spending_2018, name='inter_korean_spending_2018'),

]
