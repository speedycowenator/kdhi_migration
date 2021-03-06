from django.contrib import admin

from .models import overseas_tracker, inter_korean_tracker, overseas_topic, country_list, inter_korean_category, inter_korean_subcategory, inter_korean_level



class overseas_tracker_admin(admin.ModelAdmin):
	list_display = ('name', 'event_date', 'event_return', 'DPRK_head')

class inter_korean_tracker_admin(admin.ModelAdmin):
	list_display = ('name', 'event_date', 'DPRK_head', 'ROK_head', 'event_itteration')



admin.site.register(overseas_tracker, overseas_tracker_admin)
admin.site.register(inter_korean_tracker, inter_korean_tracker_admin)
admin.site.register(overseas_topic)
admin.site.register(inter_korean_level)
admin.site.register(inter_korean_category)
admin.site.register(inter_korean_subcategory)
admin.site.register(country_list)