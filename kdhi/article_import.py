import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kdhi.settings")
from django.conf import settings
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from trackers.models import overseas_tracker
import csv

unslugable_characters = ['.', ',', '/', '?', ';', ':', '"', "'", '|', '/', '\\', '#', '@', '$', '%', '^', '&', '*', '(', ')', '~', '`', ]

def slugify(raw_text):
	raw_text =  raw_text.lower()
	slug_temp = ''
	#for character in unslugable_characters:
	#	raw_text.replace(character, '')
	for character in raw_text:
		if character.isalpha() == True or character == ' ':
			slug_temp += character
	slug = slug_temp.replace(' ', '-')
	return(slug)



with open('kdhi_wb_ik.csv', newline='', encoding='utf-8') as csvfile:
	tracker_sheet = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in tracker_sheet:
		name 				= row[0] 
		event_description 	= row[2]
		event_coverage 		= row[3]
		slug  				= row[1]


		b = overseas_tracker(name=name, event_description=event_description, event_coverage=event_coverage, slug=slug)
		b.save()
