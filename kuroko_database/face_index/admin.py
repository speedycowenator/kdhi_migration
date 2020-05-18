from django.contrib import admin

from .models import face_instance, individual_instance

admin.site.register(face_instance)
admin.site.register(individual_instance)