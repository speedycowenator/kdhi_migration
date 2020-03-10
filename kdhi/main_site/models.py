from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect

from django.dispatch import receiver
class institution(models.Model):
    
    name                        =  models.CharField(max_length=200)
    name_korean                 =  models.CharField(max_length=200)
    tag_one                     =  models.CharField(max_length=200, blank=True) #replace iwth foreign key when able
    tag_two                     =  models.CharField(max_length=200, blank=True) #replace iwth foreign key when able
    tag_three                   =  models.CharField(max_length=200, blank=True) #replace iwth foreign key when able
    function                    =  models.CharField(max_length=2000)
    additional_information      =  models.CharField(max_length=2000, blank=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return (reverse('institution_detail', args=[str(self.name)]))

    
class individual(models.Model):
    name                    = models.CharField(max_length=200)
    name_korean             = models.CharField(max_length=200)
    icon                    = models.URLField(max_length=200, blank=True)
    full_resolution_photo   = models.URLField(max_length=200, blank=True)
    photo_credit            = models.CharField(max_length=200, blank=True)
    birthday                = models.DateField(null=True, blank=True)
    hometown                = models.CharField(max_length=200, blank=True)
    education               = models.CharField(max_length=200, blank=True)
    bio                     = models.CharField(max_length=2000, blank=True)
    sources                 = models.CharField(max_length=500, blank=True)
    video_source            = models.URLField(max_length=200, blank=True)
    video_caption           = models.CharField(max_length=200, blank=True)
    video_2_source          = models.URLField(max_length=200, blank=True)
    video_2_caption         = models.CharField(max_length=200, blank=True)
    

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return (reverse('individual_detail', args=[str(self.name)]))


    
class position(models.Model):
    person              = models.ForeignKey(individual, on_delete=models.CASCADE)
    institution         = models.ForeignKey(institution, on_delete=models.CASCADE)
    title               = models.CharField(max_length=200)   
    appointment_date    = models.DateField(null=True, blank=True)
    confirmation_date   = models.DateField(null=True, blank=True)
    confirmation_src    = models.CharField(max_length=200, default="N/A")
    replaced            = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.title


