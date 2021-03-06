"""kdhi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('state-media-archive/', include('news_archive.urls')),
    path('', include('main_site.urls')),
    path('trackers/', include('trackers.urls')),
    path('documents/', include('documents.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('search/', include('kdhi_search.urls')),
    path('video/', include('video_archive.urls')),
    path('user/', include('user.urls')),  
    path('media_archive/', include('media_archive.urls')),

]
