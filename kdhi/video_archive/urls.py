
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from . import views
from django.conf.urls import url
from video_archive import views as core_views

urlpatterns = [
    path('nanausicaa', views.nausicaa, name='nausicaa'),
]