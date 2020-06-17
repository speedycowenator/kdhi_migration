from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from main_site.models import institution, individual, position, rok_individual
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect

from django.dispatch import receiver



class subscriber(models.Model):
	name 	= models.CharField(max_length=100)
	email 	= models.EmailField(max_length=254)    

	def __str__(self):
	    return self.email
