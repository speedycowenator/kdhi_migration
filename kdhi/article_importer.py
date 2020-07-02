from bs4 import BeautifulSoup, NavigableString
import glob
import re
import bs4
import urllib.request
import datetime
import csv
import os.path
from datetime import date
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kdhi.settings")

from django.conf import settings
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

from media_archive.models import state_media_article, state_media_publication
from django.utils.html import strip_tags

row_count = 0
base_dir = 'C:/Users/Sam/Documents/GitHub/kdhi_migration/kdhi'
file_name = 'catalog_article.csv'
file_location_true = base_dir + '/' + file_name
with open(file_location_true, newline='', encoding='utf-8') as csvfile:
	tracker_sheet = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in tracker_sheet:
		if row_count == 0:
			title 		= row[0]
			content 	= row[1] 
			inst_author = row[2] 
			date 		= row[3]

			if inst_author == "Rodong Sinmun":
				publication_str = "Rodong Sinmun"
				inst_author = ''
			if inst_author == "KCNA":
				publication_str = "KCNA"
				inst_author = ''
			else:
				publication_str = "Rodong Sinmun"


		article_inst = state_media_article(
			name = title,
			text = content,
			date = date,
			language = 'EN',
			)
		article_inst.save()
		

		publication_object = state_media_publication.objects.get(name=publication_str)
		
		article_inst.publication = publication_object
		article_inst.save()
	
