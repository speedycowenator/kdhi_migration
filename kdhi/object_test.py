

import os
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kdhi.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from documents.models import document, document_collection


error_message = "retrieval failed"

'''
fuckboi_characters  	= ['?', '.', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '=', '`', '`', "'", '"', '<', '>', '/', '\\', '|', ':', ';']
document_slug  			= document_title.lower()
for character in fuckboi_characters:
	document_slug = document_slug.replace(character, '')
document_slug  			= document_slug.replace('  ', ' ')
document_slug  			= document_slug.replace(' ', '-')
'''

import csv


with open('1986_docs.csv', newline='') as csvfile:
	document_csv = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in document_csv:
		name 				= row[0]
		slug 				= row[1]
		collection 			= document_collection
		sumamry 			= row[2]
		creator 			= row[3]
		document_text 		= row[4]
		country_of_origin 	= row[5]
		document_source 	= row[6]
		print(name)
'''
document_collection_name 	= input("Article collection: ")
try: 
	document_url = document_collection.objects.get(name=document_collection_name)
	document_url = document_url.directory
	print(document_url)

except:
	print(error_message)
'''