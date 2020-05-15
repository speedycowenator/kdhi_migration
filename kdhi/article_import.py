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
	raw_text_temp = ''
	#for character in unslugable_characters:
	#	raw_text.replace(character, '')
	for character in raw_text:
		if character.isalpha() == True or character == ' ':
			raw_text_temp += character
	raw_text = raw_text_temp
	raw_text = raw_text.replace(' ', '-')
	return(raw_text)



with open('kdhi_overseas_tracker.csv', newline='', encoding='utf-8') as csvfile:
	article_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in article_reader:
		name 				= row[0] 
		event_description 	= row[2]
		event_coverage 		= row[3]
		slug  				= row[1]


		b = overseas_tracker(name=name, event_description=event_description, event_coverage=event_coverage, slug=slug)
		b.save()
