import bs4
import urllib.request
import csv
import time
from google.cloud import translate_v2 as translate
translator = translate.Client()

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kdhi.settings")
from django.conf import settings
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from media_archive.models import uritv_video
import csv
from random import randint


current = 49460
end = 49464
#end - 43000
links_range = range(current, end)
source_list = []
link_base = "http://www.uriminzokkiri.com/index.php?ptype=ccentv&mtype=view&no="
file_name                   = ''
date                        = ''
title                       = ''
title_translated            = ''
category                    = ''
category_translated         = ''
description                 = ''
description_translated      = ''
korean_keyword              = ''
english_keyword             = ''
uri_source  				= ''
db_code 					= ''

code_count = 0
for code in links_range:
	print("---------")
	if code_count < 2: 
		code_count += 1
	else:
		#time.sleep(randint(15, 3))
		time.sleep(randint(1))
		code_count = 0
		print("Waiting for Google....")
		print("---------")
	print(code)

	code = str(code)
	link = link_base + code + "#pos"
	r = urllib.request.urlopen(link)
	soup = bs4.BeautifulSoup(r, "html5lib")

	videos = soup.findAll('video')
	for video in videos:
		#print(video)
		tags = video.findAll("source") 

		tag_string = '' 
		for tag in tags:
			tag_string += str(tag)
		tag_string = tag_string.split('"')
		source = (tag_string[1])
		file_name = source

	meta_tags  = soup.findAll('meta', {'http-equiv':'keywords'})
	korean_keyword 	= []
	english_keyword = [] 
	for meta_tag in meta_tags:
		meta_tag = str(meta_tag)
		meta_tag_strip = meta_tag.split('"')
		meta_tag = meta_tag_strip[1]
		keywords = meta_tag.split(",")
		for keyword in keywords:
			language = translator.detect_language(keyword)
			print(language['input'])
			if language['language'] == 'ko':
				korean_keyword.append(keyword)

	
	title = soup.find('title').text
	if translator.detect_language(title) == 'ko':
		title_translated = translator.translate(title)
	description  = soup.find('meta', {'http-equiv':'description'})
	description = str(description)
	description_split = description.split('"')
	description_split = description_split[1]
	if translator.detect_language(description_split) == 'ko':
		description_translated = translator.translate(description_split)

#------ Category ---------	
	try: 
		category = soup.find('span', {"class":"u_tvcategname"})
		category = category.text
		category = category.strip("[")
		category = category.strip("]")
		category_translated = translator.translate(category)
		category_translated = category_translated.text
		if category_translated == "Rock painting":
			category_translated = "News Report"
	except:
		category = 'None'
		category_translated = 'None'

	print(category)
	description_translated = description_translated.text
	title_translated = title_translated.text

	file_name = source.split("/")
	slash_count = len(file_name) - 1
	file_name = file_name[slash_count]

	try:
		date = source.split("centertvall_")
		date = date[1]
		date = date.split("_")
		date = date[0]
		video = uritv_video(
			file_name                   =  file_name,
		    date                        =  date,
		    title                       =  title,
		    title_translated            =  title_translated,
		    category                    =  category,
		    category_translated         =  category_translated,
		    description                 =  description_split,
		    description_translated      =  description_translated,
		    korean_keyword              =  korean_keyword,
		    english_keyword             =  english_keyword,
		    uri_source  				=  source,
		    db_code 					=  code,
			)

		video.save()
		print("Collection Saved")
	except:
		video = uritv_video(
		file_name                   =  file_name,
	    title                       =  title,
	    title_translated            =  title_translated,
	    category                    =  category,
	    category_translated         =  category_translated,
	    description                 =  description,
	    description_translated      =  description_split,
	    korean_keyword              =  korean_keyword,
	    english_keyword             =  english_keyword,
	    uri_source  				=  source,
	    db_code 					=  code,
		)
		video.save()
		print("Collection Saved w/o Date")
