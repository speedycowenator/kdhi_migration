
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from . import views
from django.conf.urls import url
from trackers import views as core_views

urlpatterns = [
    #url('', views.search_redirect, name='redirect'),
	path('overseas_tracker/<int:pk>', views.tracker_detail, name='tracker-detail'),
	path('inter_korean_tracker/<int:pk>', views.inter_korean_tracker_detail, name='inter-korean-tracker-detail'),

]