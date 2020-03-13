from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from main_site.models import institution, individual, position
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect

from django.dispatch import receiver

class overseas_tracker(models.Model):
    #need to change function and additional information to TextField
    participant_one     =
    participant_two     =
    participant_three   =
    participant_four    =
    country_choices = (
            
         
            )
    event_description   = models.TextField(max_length=20000)
            
            
            f
            }
    
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
    


    