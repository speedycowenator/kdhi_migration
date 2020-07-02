from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

class profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.CharField(max_length=30000, blank=False, default='1')
    email_address = models.EmailField(max_length=254)
    recieve_emails = models.BooleanField(default=False)
    def __str__(self): 
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)
    instance.profile.save()
    



class nonuser_email_subscriptions(models.Model):
    email = models.EmailField(max_length=100)
    def __str__(self):
        return self.email
from django.db import models


class article_model(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    summary = models.TextField(max_length=50000, help_text='Enter a brief description of the Article')
    date_publication = models.DateField(null=True, blank=True)
    topic = models.CharField(max_length=200)



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Article-detail', args=[str(self.id)])
