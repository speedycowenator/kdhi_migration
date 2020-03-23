from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from django.dispatch import receiver

class document_collection(models.Model):
    name                        =  models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return (reverse('collection_page', args=[str(self.name)]))


class document(models.Model):
    #need to change function and additional information to TextField
    name                = models.CharField(max_length=200)
    slug                = models.CharField(max_length=200)
    collection          = models.ForeignKey(document_collection, on_delete=models.SET_NULL, null=True)
    date                = models.DateField(blank=True)
    summary             = models.TextField(max_length=20000)
    creator             = models.CharField(max_length=200)
    document_text       = models.TextField(max_length=20000, blank=True)
    url_substring       = models.CharField(max_length=200)
    country_of_origin   = models.CharField(max_length=200)
    document_source     = models.CharField(max_length=200)
    rights              = models.CharField(max_length=2000)
  
        
    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return (reverse('document_detail', args=[str(self.slug)]))
