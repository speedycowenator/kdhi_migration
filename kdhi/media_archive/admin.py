from django.contrib import admin

from django.contrib.auth.models import Group

from .models import state_media_publication, state_media_author, state_media_article

admin.site.register(state_media_publication)
admin.site.register(state_media_author)
admin.site.register(state_media_article)






