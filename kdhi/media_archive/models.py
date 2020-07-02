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
    name            = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class state_media_author(models.Model):
    name            = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class state_media_article(models.Model):
    name                = models.CharField(max_length=200)
    author              = models.CharField(max_length=200, null=True, blank=True)
    publication         = models.ForeignKey(state_media_publication, on_delete=models.SET_NULL, null=True, blank=True)
    text                = models.TextField(max_length=50000, help_text='Enter a brief description of the Article')
    date                = models.DateField(default=datetime.date.today)
    language            = models.CharField(max_length=10, default="ENG")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

class uritv_video(models.Model):
    file_name                   = models.CharField(max_length=500, null=True, blank=True)
    date                        = models.DateField(max_length=200, null=True, blank=True)
    title                       = models.CharField(max_length=500, null=True, blank=True)
    title_translated            = models.CharField(max_length=500, null=True, blank=True)
    category                    = models.CharField(max_length=200, null=True, blank=True)
    category_translated         = models.CharField(max_length=200, null=True, blank=True)
    description                 = models.CharField(max_length=2000, null=True, blank=True)
    description_translated      = models.CharField(max_length=2000, null=True, blank=True)
    korean_keyword              = models.CharField(max_length=2000, null=True, blank=True)
    korean_keyword_translated   = models.CharField(max_length=2000, null=True, blank=True)
    english_keyword             = models.CharField(max_length=2000, null=True, blank=True)
    uri_source                  = models.URLField(max_length=500, null=True, blank=True)
    db_code                     = models.CharField(max_length=2000, null=True, blank=True)
    s3_verified                 = models.BooleanField(default=False)

    def __str__(self):
        return self.db_code
    class Meta:
        ordering = ('db_code', '-date', 'title_translated') 

    def get_sourcetype(self):
        full_name = self.file_name
        file_name_split = full_name.split("_")
        sourcetype = file_name_split[0:2]
        return (sourcetype) 

    def keyword_list_korean(self):
        keyword_list = self.korean_keyword
        keyword_list = keyword_list.replace("'", "")
        keyword_list = keyword_list.replace("[", "")
        keyword_list = keyword_list.replace("]", "")
        keyword_list = keyword_list.split(",")
        return (keyword_list)


    def get_video_location(self):
        full_base   = "https://uritv-bucket.s3.amazonaws.com/"
        file_name   = self.file_name
        s3_location = full_base + file_name
        return(s3_location)

    def get_absolute_url(self):
        return reverse('video_archive_detail', args=[str(self.id)])