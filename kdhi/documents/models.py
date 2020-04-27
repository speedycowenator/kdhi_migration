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

class collection_timeline_item(models.Model):
    section_title   = models.CharField(max_length=500, blank=False)
    year            = models.IntegerField(blank=False)
    month_int       = models.FloatField(blank=False)
    month           = models.CharField(max_length=20, blank=False)
    media_src       = models.CharField(max_length=500, blank=True)
    media_text      = models.CharField(max_length=500, blank=True)

    day_1           = models.IntegerField(blank=True, null=True)
    day_1_content   = models.TextField(blank=True, null=True, max_length = 2000)

    day_2           = models.IntegerField(blank=True, null=True)
    day_2_content   = models.TextField(blank=True, null=True, max_length = 2000)

    day_3           = models.IntegerField(blank=True, null=True)
    day_3_content   = models.TextField(blank=True, null=True, max_length = 2000)

    day_4           = models.IntegerField(blank=True, null=True)
    day_4_content   = models.TextField(blank=True, null=True, max_length = 2000)

    day_5           = models.IntegerField(blank=True, null=True)
    day_5_content   = models.TextField(blank=True, null=True, max_length = 2000)

    day_6           = models.IntegerField(blank=True, null=True)
    day_6_content   = models.TextField(blank=True, null=True, max_length = 2000)

    day_7           = models.IntegerField(blank=True, null=True)
    day_7_content   = models.TextField(blank=True, null=True, max_length = 2000)

    day_8           = models.IntegerField(blank=True, null=True)
    day_8_content   = models.TextField(blank=True, null=True, max_length = 2000)

    day_9           = models.IntegerField(blank=True, null=True)
    day_9_content   = models.TextField(blank=True, null=True, max_length = 2000)

    day_10           = models.IntegerField(blank=True, null=True)
    day_10_content   = models.TextField(blank=True, null=True, max_length = 2000)

    day_11           = models.IntegerField(blank=True, null=True)
    day_11_content   = models.TextField(blank=True, null=True, max_length = 2000)

    day_12           = models.IntegerField(blank=True, null=True)
    day_12_content   = models.TextField(blank=True, null=True, max_length = 2000)

    day_13           = models.IntegerField(blank=True, null=True)
    day_13_content   = models.TextField(blank=True, null=True, max_length = 2000)


    class Meta:
        ordering = ('month_int',)
    def __str__(self):
        return self.section_title