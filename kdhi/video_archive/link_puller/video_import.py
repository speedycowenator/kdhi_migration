import bs4
import urllib.request
import csv
import time
from googletrans import Translator
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kdhi.settings")
from django.conf import settings
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from media_archive.models import uritv_video
import csv

translator = Translator()
link_base = "http://www.uriminzokkiri.com/index.php?ptype=ccentv&mtype=view&no="
code = str(35000)
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
		lang = translator.detect(keyword)
		if lang.lang == 'ko':
			korean_keyword.append(keyword)
		if lang.lang == 'en':
			english_keyword.append(keyword)
title = soup.find('title').text
if translator.detect(title).lang == 'ko':
	title_translated = translator.translate(title)
description  = soup.findAll('meta', {'http-equiv':'description'})
description = str(description)
description_split = description.split('"')
description_split = description_split[1]
if translator.detect(description_split).lang == 'ko':
	description_translated = translator.translate(description_split)
category = soup.find('span', {"class":"u_tvcategname"}).text
category = category.strip("[")
category = category.strip("]")
category_translated = translator.translate(category)
category_translated = category_translated.text
if category_translated == "Rock painting":
	category_translated = "News Report"
description_translated = description_translated.text
title_translated = title_translated.text

date = source.split("centertvall_")
date = date[1]
date = date.split("_")
date = date[0]
file_name = source.split("/")
slash_count = len(file_name) - 1
file_name = file_name[slash_count]

video = uritv_video(
	file_name                   =  file_name,
    date                        =  date,
    title                       =  title,
    title_translated            =  title_translated,
    category                    =  category,
    category_translated         =  category_translated,
    description                 =  description,
    description_translated      =  description_translated,
    korean_keyword              =  korean_keyword,
    korean_keyword_translated   =  korean_keyword_translated,
    english_keyword             =  english_keyword,
    uri_source  				=  uri_source,

	)
video.save()