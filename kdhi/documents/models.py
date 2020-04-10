from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from django.dispatch import receiver

class document_collection(models.Model):
    name                        = models.CharField(max_length=200)
    directory                   = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return (reverse('collection_page', args=[str(self.name)]))

    class Meta:
        ordering = ('name',)
  

class document(models.Model):
    #need to change function and additional information to TextField
    name                = models.CharField(max_length=200)
    slug                = models.CharField(max_length=200)
    url_substring       = models.CharField(max_length=200, blank=True, default='https://kdhi-resources.s3.amazonaws.com/kdhi.org/Assets/Documents/')
    collection          = models.ForeignKey(document_collection, on_delete=models.SET_NULL, null=True, blank=True)
    date                = models.DateField(blank=True)
    summary             = models.TextField(max_length=20000)
    creator             = models.CharField(max_length=200, blank=True)
    document_text       = models.TextField(max_length=20000, blank=True)
    country_of_origin   = models.CharField(max_length=200, blank=True)
    document_source     = models.CharField(max_length=200, blank=True)
    rights              = models.CharField(max_length=2000, blank=True)
    index_outdated      = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ('name',)
    
        
    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return (reverse('document_detail', args=[str(self.slug)]))
