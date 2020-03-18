from django.contrib import admin


from .models import document, document_collection
admin.site.register(document)
admin.site.register(document_collection)

