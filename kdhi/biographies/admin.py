from django.contrib import admin

from .models import individual, institution, position

admin.site.register(individual)
admin.site.register(institution)
admin.site.register(position)