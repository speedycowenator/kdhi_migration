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
import boto3
from decimal import Decimal
import json
import urllib
import os

now = date.today()

#---------- Similarity (through model - or just run a search every time? Is there a usecase for needing to get a static
#page that lists similar photos? No, these would be returning a search so no reason to build. 

#---------- FACE (unique face ID associated with each input photo)
class face_instance(models.Model):
	kuroko_id 			= models.CharField(max_length=200)
	src_image 			= models.CharField(max_length=200) #eventually want to link to KCNA stream (date plus timestamp) 
	individual_match 	= models.ForeignKey(
		'individual_instance',
		on_delete=models.PROTECT,
		)
	image_quality 		= models.PositiveSmallIntegerField(default=0)	
	#measure of face resolution, use to weigh significance of two matches 

	def __str__(self):
		return self.kuroko_id



#---------- INDIVIDUAL (person a face is linked to. Every face has an individual, but an individual can have multiple faces)
class individual_instance(models.Model):
	name 			= models.CharField(max_length=100, blank=True)
	benchmark_pic 	= models.CharField(max_length=100, blank=True)
	assc_face 		= models.ManyToManyField('face_instance', related_name="individual_face")

	def __str__(self):
		return str(self.	pk)


#class example_model(models.Model):
#	models.CharField(max_length=200)
#    def __str__(self):
#        return self.slug
#    def get_absolute_url(self):
#        return (reverse('url_name', args=[str(self.lookup_argument)])) 