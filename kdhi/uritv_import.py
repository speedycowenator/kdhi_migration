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

current = 36000
end = 36500
#current = 49430
#end = 49464

links_range = range(current, end)
source_list = []
link_base = "http://www.uriminzokkiri.com/index.php?ptype=ccentv&mtype=view&no="
failed_codes = []

code_count = 0
for code in links_range:
	code = str(code)
	try: 
		link = link_base + code + "#pos"
		r = urllib.request.urlopen(link)
		soup = bs4.BeautifulSoup(r, "html5lib")

		videos = soup.findAll('video')
		for video in videos:
			tags = video.findAll("source") 
			tag_string = '' 
			for tag in tags:
				tag_string += str(tag)
			tag_string = tag_string.split('"')
			source = (tag_string[1])
			file_name = source

		meta_tags  = soup.findAll('meta', {'http-equiv':'keywords'})
		for meta_tag in meta_tags:
			meta_tag = str(meta_tag)
			meta_tag_strip = meta_tag.split('"')
			meta_tag = meta_tag_strip[1]
			keywords = meta_tag.split(",")
		keywords_korean = []
		for key_tag in keywords:
			language = translator.detect_language(key_tag)
			if language['language'] == 'ko':
				key_tag = key_tag.replace(" ", "")
				key_tag = key_tag.replace("'", "")
				keywords_korean.append(key_tag)


		title = soup.find('title').text

		description  = soup.find('meta', {'http-equiv':'description'})
		description = str(description)
		description_split = description.split('"')
		description_split = description_split[1]

		try:
			category = soup.find('span', {"class":"u_tvcategname"}).text
			category = category.strip("[")
			category = category.strip("]")
		except:
			pass
		file_name = source.split("/")
		slash_count = len(file_name) - 1
		file_name = file_name[slash_count]


		date_steps = file_name
		date_steps = date_steps.split("_")
		count_date_steps = len(date_steps)
		date_steps_location = count_date_steps -2 
		date = date_steps[date_steps_location]

		video = uritv_video(
			file_name                   = file_name,
			date 						= date,
			title                       = title,
			category                    = category,
			description                 = description_split,
			uri_source  				= source,
			db_code 					= code,
			korean_keyword 				= keywords_korean,
			)

		video.save()
		print(code)
		print("Collection Saved")
		print("---------------------")
	except:
		print("Collection for {} Failed".format(code))
		failed_codes.append(code)
print(failed_codes)