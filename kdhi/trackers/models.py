from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from main_site.models import institution, individual, position, rok_individual
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect

from django.dispatch import receiver

class overseas_tracker(models.Model):
    #need to change function and additional information to TextField
    participant_DPRK     = models.ManyToManyField(individual)
    country_choices = (
            
         
            )
    event_description   = models.TextField(max_length=20000)
    event_title         = models.CharField(max_length=200)
    event_date          = models.DateField(null=True, blank=True)
    event_photo         = models.URLField(max_length=200, blank=True)
    event_photo_add_1   = models.URLField(max_length=200, blank=True)
    event_photo_add_2   = models.URLField(max_length=200, blank=True)
    event_photo_add_3   = models.URLField(max_length=200, blank=True)

    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return (reverse('tracker_detail', args=[str(self.title)]))
    


class inter_korean_tracker(models.Model):
    #need to change function and additional information to TextField
    participant_ROK    = models.ManyToManyField(rok_individual)
    participant_DPRK     = models.ManyToManyField(individual)

    country_choices = (
            
         
            )
    event_description   = models.TextField(max_length=20000)
    event_title         = models.CharField(max_length=200)
    event_date          = models.DateField(null=True, blank=True)
    event_photo         = models.URLField(max_length=200, blank=True)
    event_photo_add_1   = models.URLField(max_length=200, blank=True)
    event_photo_add_2   = models.URLField(max_length=200, blank=True)
    event_photo_add_3   = models.URLField(max_length=200, blank=True)

    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return (reverse('tracker_detail', args=[str(self.title)]))
    


        