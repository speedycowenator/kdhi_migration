from django.contrib import admin
from django.contrib.auth.models import Group

from .models import individual, institution, position, rok_position, rok_institution, rok_individual, article, glossary_item


class positionAdmin(admin.ModelAdmin):
	list_display = ('person', 'institution', 'title', 'position_status')
	list_filter  = ('created_at', 'updated_at', 'position_status', 'title', 'institution')


class ROKpositionAdmin(admin.ModelAdmin):
	list_display = ('person', 'institution', 'title')

admin.site.register(individual) 
admin.site.register(institution)
admin.site.register(position, positionAdmin)
admin.site.register(rok_individual)
admin.site.register(rok_institution)
admin.site.register(rok_position, ROKpositionAdmin)
admin.site.register(article)
admin.site.register(glossary_item)

