from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from . import views
from django.conf.urls import url
from user import views as core_views

urlpatterns = [
	path('subscribe/', views.email_signup, name='email_signup'),
	path('form-test', views.form_test, name='form_test'),
    ]