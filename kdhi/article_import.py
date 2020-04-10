import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kdhi.settings")
from django.conf import settings
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from documents.models import document
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



with open('1987_documents.csv', newline='', encoding='utf-8') as csvfile:
	article_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in article_reader:
		'''
		date_fixed = ''
		date = row[1]
		for character in date:
			if character == '/':
				character = '-'
			date_fixed += character
		date_fixed_list = date_fixed.split('-')
		date_fixed = date_fixed_list[2] + '-' + date_fixed_list[0] + '-' + date_fixed_list[1]
		date 	= date_fixed
		'''
		title 	= row[0]
		slug 	= slugify(title)
		date  	= row[1]
		summary = row[2]

		b = document(name=title, summary=summary, date=date, slug=slug)
		b.save()
