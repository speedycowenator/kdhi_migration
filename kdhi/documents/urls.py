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
	path('timeline/<int:init_year>-<int:end_year>', views.timeline, name='timeline'),
	path('document-collection/<str:name>', views.document_list, name='document_list'),
    ]