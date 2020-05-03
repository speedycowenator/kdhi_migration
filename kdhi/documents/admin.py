from django.contrib import admin

from django.contrib.auth.models import Group

from .models import document, document_collection, collection_timeline_item, critical_oral_history
class documentAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'creator', 'date')
	list_filter  = ('country_of_origin', 'collection', 'document_source')
admin.site.register(document, documentAdmin)
admin.site.register(document_collection)
admin.site.register(collection_timeline_item)
admin.site.register(critical_oral_history)





