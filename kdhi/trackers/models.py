from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from main_site.models import institution, individual, position, rok_individual
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect

from django.dispatch import receiver

class country_list(models.Model):
    country             = models.CharField(max_length=100)
    
    def __str__(self):
        return self.country

class overseas_topic(models.Model):
    topic               = models.CharField(max_length=100)
    
    def __str__(self):
        return self.topic


class overseas_tracker(models.Model):
    #need to change function and additional information to TextField
    name                = models.CharField(max_length=200)
    DPRK_head           = models.ForeignKey(individual, on_delete=models.PROTECT, related_name = 'dprk_overseas_head', null=True, blank=True)
    participant_DPRK    = models.ManyToManyField(individual)
    country_choices     = models.ForeignKey(country_list, on_delete=models.PROTECT, null=True, blank=True)
    overseas_topics     = models.ForeignKey(overseas_topic, on_delete=models.PROTECT, null=True, blank=True)
    event_document      = models.URLField(max_length=200, blank=True)
    event_description   = models.TextField(max_length=20000)
    event_date          = models.DateField(null=True, blank=True)
    event_photo         = models.URLField(max_length=200, blank=True)
    event_photo_add_1   = models.URLField(max_length=200, blank=True)
    event_photo_add_2   = models.URLField(max_length=200, blank=True)
    event_photo_add_3   = models.URLField(max_length=200, blank=True)
    update_date         = models.DateField(auto_now=True)

    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return (reverse('overseas_tracker_detail', args=[int(self.pk)]))
    


class inter_korean_tracker(models.Model):
    #need to change function and additional information to TextField
    name                = models.CharField(max_length=200)
    ROK_head            = models.ForeignKey(rok_individual, on_delete=models.PROTECT, related_name = 'rok_head', null=True, blank=True)
    DPRK_head           = models.ForeignKey(individual, on_delete=models.PROTECT, related_name = 'dprk_head', null=True, blank=True)
    participant_ROK     = models.ManyToManyField(rok_individual, related_name = 'rok_delegation', blank=True, default="Kim Jong Un")
    participant_DPRK    = models.ManyToManyField(individual, related_name = 'dprk_delegation', blank=True)
    MOU_description     = models.TextField(max_length=20000)
    event_location      = models.CharField(max_length=200)
    event_venue         = models.CharField(max_length=200)
    event_date          = models.DateField(null=True, blank=True)
    document_link       = models.URLField(max_length=200, blank=True)
    event_photo         = models.URLField(max_length=200, blank=True)
    event_photo_add_1   = models.URLField(max_length=200, blank=True)
    event_photo_add_2   = models.URLField(max_length=200, blank=True)
    event_photo_add_3   = models.URLField(max_length=200, blank=True)
    update_date          = models.DateField(auto_now=True)

    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return (reverse('inter_korean_tracker_detail', args=[int(self.pk)]))
    


        