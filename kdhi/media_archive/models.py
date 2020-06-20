from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect

from django.dispatch import receiver
from djrichtextfield.models import RichTextField
from datetime import date, timedelta
now = date.today()
import bs4
import urllib.request

import datetime

class state_media_publication(models.Model):
	name 			= models.CharField(max_length=200)

	def __str__(self):
		return self.name

class state_media_author(models.Model):
	name 			= models.CharField(max_length=200)

	def __str__(self):
		return self.name

class state_media_article(models.Model):
	name 				= models.CharField(max_length=200)
	author 				= models.ForeignKey(state_media_author, on_delete=models.SET_NULL, null=True, blank=True)
	publication 		= models.ForeignKey(state_media_publication, on_delete=models.SET_NULL, null=True, blank=True)
	text 				= models.TextField(max_length=50000, help_text='Enter a brief description of the Article')
	date 				= models.DateField(default=datetime.date.today)
	language 			= models.CharField(max_length=10, default="ENG")

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('article-detail', args=[str(self.id)])
