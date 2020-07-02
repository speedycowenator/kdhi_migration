from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect

from django.dispatch import receiver
from djrichtextfield.models import RichTextField
from datetime import date, timedelta
import bs4
import urllib.request
from main_site.models import institution, individual, position, rok_individual

now = date.today()
#     cd documents/github/kdhi_migration/kdhi

class figure(models.Model):
	name 			= models.CharField(max_length=100)
	kdhi_db_figure 	= models.ForeignKey(individual, null=True, blank=True, on_delete=models.CASCADE)
   
	class Meta:
		ordering = ('name',) 
		
	def __str__(self):
		return self.name

class face(models.Model):
	name    		= models.CharField(max_length=100)
	verified_figure = models.ForeignKey(figure, blank=True, on_delete=models.SET_NULL, related_name="index_figure", null=True)
	assc_figure     = models.ManyToManyField(figure, through="face_to_figure_link",  blank=True)
	image_filename  = models.CharField(max_length=100, null=True, blank=True)
	image_quality 	= models.IntegerField(blank=True, null=True)
	
	class Meta:
		ordering = ('name',) 
		
	def __str__(self):
		return self.name

class face_to_figure_link(models.Model):
	face 		= models.ForeignKey(face, blank=True, on_delete=models.SET_NULL, null=True)
	figure 		= models.ForeignKey(figure, blank=True, on_delete=models.SET_NULL, null=True)
	similarity 	= models.IntegerField(blank=True)