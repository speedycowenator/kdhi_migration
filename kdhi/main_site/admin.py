from django.contrib import admin


from .models import individual, institution, position, rok_position, rok_institution, rok_individual, article, glossary_item

admin.site.register(individual)
admin.site.register(institution)
admin.site.register(position)
admin.site.register(rok_individual)
admin.site.register(rok_institution)
admin.site.register(rok_position)
admin.site.register(article)
admin.site.register(glossary_item)

