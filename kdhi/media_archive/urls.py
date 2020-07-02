from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from . import views
from django.conf.urls import url
from media_archive import views as core_views

urlpatterns = [
	path('article/<int:pk>', views.article_detail, name='article_detail'),
	path('state-media-video-archive/<int:pk>', views.video_archive_detail, name='video_archive_detail'),
	path('article', views.article_list, name='article_list'),
	path('state-media-video-archive', views.video_archive_list, name='video_archive_list'),
    ]