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

class dprk_institution_tag(models.Model):
    name    = models.CharField(max_length=21)
    weight  = models.IntegerField()
   
    class Meta:
        ordering = ('-weight', 'name') 
        
    def __str__(self):
        return self.name


class glossary_item(models.Model):
    name                       = models.CharField(max_length=200)
    slug                        = models.CharField(max_length=200)
    image_src                   = models.CharField(max_length=200)
    bluff_content               = models.CharField(max_length=500)
    content                     = RichTextField()
    update_date = models.DateField(auto_now=True)
    class Meta:
        ordering = ('name',)   
 
    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return (reverse('glossary_detail', args=[str(self.slug)])) 


class institution(models.Model):
    #need to change function and additional information to TextField
    name                        =  models.CharField(max_length=200)
    name_korean                 =  models.CharField(max_length=200)
    tripartite_tag              =  models.CharField(max_length=200, blank=True) #replace iwth foreign key when able
    function_tags               =  models.ManyToManyField(dprk_institution_tag, blank=True, null=True)
    function                    =  RichTextField(null=True, blank=True)
    additional_figures          =  RichTextField(null=True, blank=True)
    organization_structure      =  RichTextField(null=True, blank=True)
    additional_information      =  RichTextField(null=True, blank=True)
    sources_add                 =  RichTextField(null=True, blank=True, default='''<a href="https://nkinfo.unikorea.go.kr/nkp/main/portalMain.do">[1]</a> Ministry of Unification, '2019년 북한 기관별 인명록'  2018-12-27' Party of Korea (WPK)''')
    update_date = models.DateField(auto_now=True)
    class Meta:
        ordering = ('name',)   
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return (reverse('institution_detail', args=[str(self.name)]))

    
class individual(models.Model):
    name                    = models.CharField(max_length=200)
    name_korean             = models.CharField(max_length=200)
    photo_credit            = models.CharField(max_length=200, blank=True)
    birthday                = models.DateField(null=True, blank=True)
    hometown                = models.CharField(max_length=200, blank=True)
    education               = models.CharField(max_length=200, blank=True)
    bio                     = models.TextField(max_length=20000, blank=True)
    sources                 = models.TextField(max_length=500, blank=True)
    video_source            = models.URLField(max_length=200, blank=True)
    video_caption           = models.CharField(max_length=200, blank=True)
    video_2_source          = models.URLField(max_length=200, blank=True)
    video_2_caption         = models.CharField(max_length=200, blank=True)
    update_date             = models.DateField(auto_now=True)

    class Meta:
        ordering = ('name',)
  

    def __str__(self):
        return self.name
   
    def get_absolute_url(self):
        return (reverse('individual_detail', args=[str(self.name)]))
  
    def get_image_full(self):
        full_base   = "https://kdhi-resources.s3.amazonaws.com/kdhi.org/Assets/Leadership+Photos/Full+Resolution/"
        full_suffix = '.jpg'
        image_name  = self.name.replace(' ', '+')
        full_string = full_base + image_name + full_suffix
        try: 
            webpage=str(urllib.request.urlopen(full_string).read())
            soup = bs4.BeautifulSoup(webpage, features = "lxml")
        except:
            full_string = full_base + "1_Outline_Blank" + full_suffix
        return full_string
  
    def get_image_icon(self):
        icon_base   = "https://kdhi-resources.s3.amazonaws.com/kdhi.org/Assets/Leadership+Photos/1+x+1+Icons/"
        icon_suffix = '.jpg'
        image_name  = self.name.replace(' ', '+')
        icon_string = icon_base + image_name + icon_suffix       
        try:
            webpage=str(urllib.request.urlopen(icon_string).read())
            soup = bs4.BeautifulSoup(webpage, features = "lxml")
        except:
            icon_string = icon_base + "1_Outline_Blank" + icon_suffix
        return icon_string

    def bs4_image_test(self):
        full_base   = "https://kdhi-resources.s3.amazonaws.com/kdhi.org/Assets/Leadership+Photos/Full+Resolution/"
        full_suffix = '.jpg'
        image_name  = self.name.replace(' ', '+')
        full_string = full_base + image_name + full_suffix
        try: 
            webpage=str(urllib.request.urlopen(full_string).read())
            soup = bs4.BeautifulSoup(webpage, features = "lxml")
        except:
            full_string = full_base + "1_Outline_Blank" + full_suffix
        return full_string
    
class position(models.Model):
    person              = models.ForeignKey(individual, on_delete=models.CASCADE)
    institution         = models.ForeignKey(institution, on_delete=models.CASCADE)
    title               = models.CharField(max_length=200)   
    appointment_date    = models.DateField(null=True, blank=True)
    confirmation_date   = models.DateField(null=True, blank=True, default="2020-05-13")
    confirmation_src    = models.CharField(max_length=200, blank=True, default="MOU Report")
    created_at          = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at          = models.DateTimeField(auto_now=True, null=True, blank=True)
    position_rank       = models.IntegerField(null=False, blank=False, default=0)
    update_date = models.DateField(auto_now=True)

    ACTIVE      = "Active"  
    UNCLEAR     = "Unclear"
    REMOVED     = "Removed"
    LIKELY      = "Likely"

    position_status_choices = [
        (ACTIVE, "Active"),
        (LIKELY, "Likely"),
        (UNCLEAR, "Unclear"),
        (REMOVED, "Removed"),

        ]

    position_status     = models.CharField(
        choices=position_status_choices,
        default=ACTIVE,
        max_length=20
        )



    def __str__(self):
        return self.title
    class Meta:
        ordering = ('position_rank', 'person')
      
    
class rok_institution(models.Model):
    #need to change function and additional information to TextField
    name                        =  models.CharField(max_length=200)
    slug                        =  models.CharField(max_length=200)
    official_webpage            =  models.URLField(max_length=300, blank=True)
    name_korean                 =  models.CharField(max_length=200)
    tag_one                     =  models.CharField(max_length=200, blank=True) #replace iwth foreign key when able
    tag_two                     =  models.CharField(max_length=200, blank=True) #replace iwth foreign key when able
    tag_three                   =  models.CharField(max_length=200, blank=True) #replace iwth foreign key when able
    function                    =  models.TextField(max_length=20000, blank=True)
    history                     =  models.TextField(max_length=20000, blank=True)
    qs_slug                     =  models.TextField(max_length=250, blank=False, default='SLUG MISSING')
    sources_add                 =  models.TextField(max_length=20000, blank=True, default='[*] Official Ministry Website')
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
      

    def get_absolute_url(self):
        return (reverse('rok_institution_detail', args=[str(self.slug)]))



    
class rok_individual(models.Model):
    name                    = models.CharField(max_length=200)
    name_slug               = models.CharField(max_length=200)

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
    sources                 = models.TextField(max_length=500, default='[*] Official Ministry Website')
    video_source            = models.URLField(max_length=200, blank=True)
    video_caption           = models.CharField(max_length=200, blank=True)
    video_2_source          = models.URLField(max_length=200, blank=True)
    video_2_caption         = models.CharField(max_length=200, blank=True)
    update_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ('name',)
  

    def __str__(self):
        return self.name_slug
    def get_image_icon(self):
        icon_base   = 'https://kdhi-resources.s3.amazonaws.com/kdhi.org/Assets/ROK+Government+Assets/icon/'
        icon_suffix = '.jpg'
        icon_string = icon_base + self.name_slug + icon_suffix
        try:
            webpage=str(urllib.request.urlopen(icon_string).read())
            soup = bs4.BeautifulSoup(webpage, features = "lxml")
        except:
            icon_string = icon_base + "1_Outline_Blank" + icon_suffix
        return icon_string
        
    def get_absolute_url(self):
        return (reverse('rok_individual_detail', args=[str(self.name_slug)]))



    
class rok_position(models.Model):   
    person              = models.ForeignKey(rok_individual,  on_delete=models.SET_NULL, null=True)
    institution         = models.ForeignKey(rok_institution, on_delete=models.SET_NULL, null=True)
    title               = models.CharField(max_length=200)   
    appointment_date    = models.DateField(null=True, blank=True)
    confirmation_date   = models.DateField(null=True, blank=True)
    confirmation_src    = models.CharField(max_length=200, default="N/A")
    replaced            = models.CharField(max_length=200, blank=True)
    position_rank       = models.IntegerField(null=False, blank=False, default=0)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ('position_rank', 'person')

class article(models.Model):
    name        = models.CharField(max_length=200)
    slug        = models.CharField(max_length=200)
    icon_image  = models.CharField(max_length=200)
    bluff       = models.TextField(max_length=5000)
    author      = models.CharField(max_length=50, default="KDHI")
    content     = RichTextField()
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.slug
    def get_absolute_url(self):
        return (reverse('article_detail', args=[str(self.slug)]))


