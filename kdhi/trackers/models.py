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
    class Meta:
        ordering = ('country',)


class overseas_topic(models.Model):
    topic               = models.CharField(max_length=100)
    
    def __str__(self):
        return self.topic
    class Meta:
        ordering = ('topic',)

class overseas_tracker(models.Model):
    #need to change function and additional information to TextField
    name                = models.CharField(max_length=500)
    slug                = models.CharField(max_length=500, null=True, blank=True)
    DPRK_head           = models.ForeignKey(individual, on_delete=models.PROTECT, related_name = 'dprk_overseas_head', null=True, blank=True)
    participant_DPRK    = models.ManyToManyField(individual, blank=True)
    country_choices     = models.ManyToManyField(country_list, blank=True)
    overseas_topics     = models.ManyToManyField(overseas_topic, blank=True)
    event_document      = models.URLField(max_length=200, blank=True)
    event_coverage      = models.URLField(max_length=200, blank=True)
    event_description   = models.TextField(max_length=20000)
    event_date          = models.DateField(null=True, blank=True)
    event_return        = models.DateField(null=True, blank=True)
    event_photo         = models.URLField(max_length=200, blank=True)
    event_photo_credit  = models.CharField(max_length=100, blank=False, default="MOU")
    event_photo_add_1   = models.URLField(max_length=200, blank=True)
    event_photo_add_2   = models.URLField(max_length=200, blank=True)
    event_photo_add_3   = models.URLField(max_length=200, blank=True)
    update_date         = models.DateField(auto_now=True)
    created_date          = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    class Meta:
        ordering = ('-event_date', 'name',)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return (reverse('overseas_tracker_detail', args=[str(self.slug)]))
    


class inter_korean_category(models.Model):
    name                = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class inter_korean_subcategory(models.Model):
    name                = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class inter_korean_level(models.Model):
    name                = models.CharField(max_length=500) 

    def __str__(self):
        return self.name

class inter_korean_tracker(models.Model):
    #need to change function and additional information to TextField
    name                = models.CharField(max_length=500)
    slug                = models.CharField(max_length=500, blank=True)
    event_category      = models.ForeignKey(inter_korean_category, on_delete=models.PROTECT, related_name = 'event_category', null=True, blank=True)
    event_subcategory   = models.ManyToManyField(inter_korean_subcategory, related_name = 'event_subcategory', blank=True)
    event_level         = models.ForeignKey(inter_korean_level, on_delete=models.PROTECT, related_name = 'event_level', null=True, blank=True)
    ROK_head            = models.ForeignKey(rok_individual, on_delete=models.PROTECT, related_name = 'rok_head', null=True, blank=True)
    DPRK_head           = models.ForeignKey(individual, on_delete=models.PROTECT, related_name = 'dprk_head', null=True, blank=True)
    participant_ROK     = models.ManyToManyField(rok_individual, related_name = 'rok_delegation', blank=True)
    participant_DPRK    = models.ManyToManyField(individual, related_name = 'dprk_delegation', blank=True)
    meeting_topics      = models.ManyToManyField(overseas_topic, blank=True)
    MOU_description     = models.TextField(max_length=20000)
    event_venue         = models.CharField(max_length=200)
    event_date          = models.DateField(null=True, blank=True)
    event_end_date      = models.DateField(null=True, blank=True)
    document_link       = models.CharField(max_length=500, blank=True)
    document_name       = models.CharField(max_length=1000, default="No Document Available")
    event_photo         = models.CharField(max_length=500, blank=True)
    event_photo_add_1   = models.CharField(max_length=500, blank=True)
    event_photo_add_2   = models.CharField(max_length=500, blank=True)
    event_photo_add_3   = models.CharField(max_length=500, blank=True)
    update_date         = models.DateField(auto_now=True)
    created_date        = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    event_photo_credit  = models.CharField(max_length=100, blank=False, default="MOU")
    event_itteration    = models.CharField(max_length=2, default="1")
    media_coverage      = models.CharField(max_length=500, blank=True)


 
    class Meta:
        ordering = ('event_date', 'name',)
     
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return (reverse('inter_korean_tracker_detail', args=[str(self.slug), int(self.event_itteration)]))
    


        