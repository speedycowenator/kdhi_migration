
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from . import views
from django.conf.urls import url
from news_archive import views as core_views

urlpatterns = [
    #url('', views.search_redirect, name='redirect'),
	path('article/<int:pk>', views.ArticleDetailView, name='Article-detail'),
	path('search-results/', views.search_results, name='search_results'),
	url(r'^accounts/', include('django.contrib.auth.urls')),
	path('accounts/profile/', views.profile_page, name='profile'),
    url(r'signup/$', core_views.signup, name='signup'),
    path('accounts/profile/update/', views.ProfileUpdate, name='Update Profile'),
    path('no_account_subscribe', views.no_account_subscribe, name='no_account_subscribe'),
    path('accounts/print_list/', views.print_list, name='print_list')
]
