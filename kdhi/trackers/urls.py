
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from . import views
from django.conf.urls import url
from trackers import views as core_views

urlpatterns = [
    #url('', views.search_redirect, name='redirect'),
	path('overseas_tracker', views.overseas_tracker_list, name='overseas_tracker_list'),
	path('overseas_tracker/<int:pk>', views.overseas_tracker_detail, name='overseas_tracker_detail'),
	path('inter_korean_tracker', views.inter_korean_tracker_list, name='inter_korean_tracker_list'),
	path('inter_korean_tracker/<int:pk>', views.inter_korean_tracker_detail, name='inter_korean_tracker_detail'),
	path('heatmap_static', views.heatmap_static, name='heatmap_static'),



	
]