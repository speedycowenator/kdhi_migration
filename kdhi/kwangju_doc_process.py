import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kdhi.settings")
from django.conf import settings
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from documents.models import document, document_collection
import csv
import string

unslugable_characters = ['.', ',', '/', '?', ';', ':', '"', "'", '|', '/', '\\', '#', '@', '$', '%', '^', '&', '*', '(', ')', '~', '`', ]
rok = 'rok'
dprk = 'dprk'

slugcheck_characters = ['.', ',', '"', "'", '#', '@', '$', '%', '^', '&', '*', '(', ')', '~', '`', ]


def s3_slugify(raw_text):
	slug_temp = raw_text
	slug = slug_temp.replace(' ', '+')
	return(slug)

row_count = 0
base_dir = 'C:/Users/Sam/Documents/GitHub/kdhi_migration/kdhi'
file_name = 'kwangju_docs.csv'
file_location_true = base_dir + '/' + file_name
with open(file_location_true, newline='', encoding='utf-8') as csvfile:
	tracker_sheet = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in tracker_sheet:
		if row_count == 0:
			#row_count = 1  
			# Enable the row_count line to limit import to a single item
			document_title					= row[0] 
			document_date					= row[1] 
			document_origin					= row[2]
			foia_rd							= row[3]
			document_title_slug 			= s3_slugify(document_title)
			import_collection_object 		= document_collection.objects.get(name='1980 Gwangju Massacre')

			kwangju_document = document(
			 	name                = document_title,
			 	summary 			= "No document summary currently available.",
			    slug                = document_title_slug,
			    date                = document_date,
			    creator             = document_origin,
			    country_of_origin   = "United States",
			    document_source     = "US Department of State",
			    rights              = "https://foia.state.gov/Search/Results.aspx?collection=Kwangju",
			    collection 			= import_collection_object,
		)
				
			kwangju_document.save()
			