from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from . import views
from django.conf.urls import url
from media_archive import views as core_views

urlpatterns = [
	path('article/<int:pk>', views.article_detail, name='article-detail'),
    ]