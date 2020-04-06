from django.contrib import admin

from django.contrib.auth.models import Group

from .models import document, document_collection
class documentAdmin(admin.ModelAdmin):
	list_display = ('name', 'creator', 'date')
	list_filter  = ('country_of_origin', 'collection', 'document_source')
admin.site.register(document, documentAdmin)
admin.site.register(document_collection)



