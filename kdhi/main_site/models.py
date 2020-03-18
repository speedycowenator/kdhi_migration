from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect

from django.dispatch import receiver
from djrichtextfield.models import RichTextField

class institution(models.Model):
    #need to change function and additional information to TextField
    name                        =  models.CharField(max_length=200)
    name_korean                 =  models.CharField(max_length=200)
    tag_one                     =  models.CharField(max_length=200, blank=True) #replace iwth foreign key when able
    tag_two                     =  models.CharField(max_length=200, blank=True) #replace iwth foreign key when able
    tag_three                   =  models.CharField(max_length=200, blank=True) #replace iwth foreign key when able
    function                    =  models.TextField(max_length=20000)
    additional_information      =  models.TextField(max_length=20000, blank=True)
    
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
    bio                     = models.TextField(max_length=20000)
    sources                 = models.TextField(max_length=500)
    video_source            = models.URLField(max_length=200, blank=True)
    video_caption           = models.CharField(max_length=200, blank=True)
    video_2_source          = models.URLField(max_length=200, blank=True)
    video_2_caption         = models.CharField(max_length=200, blank=True)
    class Meta:
        ordering = ('name',)
  

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
    
    
class rok_institution(models.Model):
    #need to change function and additional information to TextField
    name                        =  models.CharField(max_length=200)
    name_korean                 =  models.CharField(max_length=200)
    tag_one                     =  models.CharField(max_length=200, blank=True) #replace iwth foreign key when able
    tag_two                     =  models.CharField(max_length=200, blank=True) #replace iwth foreign key when able
    tag_three                   =  models.CharField(max_length=200, blank=True) #replace iwth foreign key when able
    function                    =  models.TextField(max_length=20000, blank=True)
    history                     =  models.TextField(max_length=20000, blank=True)
    additional_information      =  models.TextField(max_length=20000, blank=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return (reverse('rok_institution_detail', args=[str(self.name)]))



    
class rok_individual(models.Model):
    name                    = models.CharField(max_length=200)
    name_true               = models.CharField(max_length=200)

    name_korean             = models.CharField(max_length=200, blank=True)
    icon                    = models.URLField(max_length=200, blank=True)
    full_resolution_photo   = models.URLField(max_length=200, blank=True)
    photo_credit            = models.CharField(max_length=200, blank=True)
    birthday                = models.DateField(null=True, blank=True)
    hometown                = models.CharField(max_length=200, blank=True)
    education_items         = models.TextField(max_length=20000, blank=True)
    education_timeline      = models.TextField(max_length=20000, blank=True)
    career_items            = models.TextField(max_length=20000, blank=True)
    career_timeline         = models.TextField(max_length=20000, blank=True)
    awards_items            = models.TextField(max_length=20000, blank=True)
    awards_timeline         = models.TextField(max_length=20000, blank=True)
    sources                 = models.TextField(max_length=500)
    video_source            = models.URLField(max_length=200, blank=True)
    video_caption           = models.CharField(max_length=200, blank=True)
    video_2_source          = models.URLField(max_length=200, blank=True)
    video_2_caption         = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ('name',)
  

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return (reverse('individual_detail', args=[str(self.name)]))
    
class article(models.Model):
    content = RichTextField()
    

    
class rok_position(models.Model):   
    person              = models.ForeignKey(rok_individual,  on_delete=models.SET_NULL, null=True)
    institution         = models.ForeignKey(rok_institution, on_delete=models.SET_NULL, null=True)
    title               = models.CharField(max_length=200)   
    appointment_date    = models.DateField(null=True, blank=True)
    confirmation_date   = models.DateField(null=True, blank=True)
    confirmation_src    = models.CharField(max_length=200, default="N/A")
    replaced            = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.title


