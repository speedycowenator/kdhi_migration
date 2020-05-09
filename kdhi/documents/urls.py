from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from . import views
from django.conf.urls import url
from main_site import views as core_views

urlpatterns = [
    #url('', views.search_redirect, name='redirect'),
	path('document/<str:slug>', views.document_detail, name='document_detail'),
	path('collection/<str:name>', views.collection_page, name='collection_page'),
	path('document-collection/<str:name>', views.document_list, name='document_list'),
	path('', views.korean_democratization_project_landing, name='korean_democratization_project_landing'),
	path('document', views.documents_landing, name='documents_landing'),
	path('timeline', views.timelines_landing, name='timelines_landing'),
	path('timeline-collection/<str:name>', views.collection_timeline, name='collection_timeline'),
	path('timeline-chronological/<int:init_year>-<int:end_year>', views.timeline_chrono, name='timeline_chrono'),
	path('critical-oral-history/<str:session>', views.critical_oral_history_detail, name='critical_oral_history'),
	path('critical-oral-history', views.critical_oral_history_landing, name='critical_oral_history_landing'),
	path('document-search', views.document_search, name='document_search'),
    ]