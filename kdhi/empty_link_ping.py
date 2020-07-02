
import bs4
import requests
import csv
import time
from google.cloud import translate_v2 as translate
translator = translate.Client()
from datetime import date, timedelta
import bs4
import urllib.request

now = date.today()
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kdhi.settings")
from django.conf import settings
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from media_archive.models import uritv_video
import csv
from random import randint
download_pending_list = []
links_range = []
link_range_max = 50
link_counter = 0
unverified_uritv_list = uritv_video.objects.filter(s3_verified=False)
for unverified_code in unverified_uritv_list:
	if link_counter < link_range_max:
		links_range.append(unverified_code.db_code)
		link_counter += 1
list_length = len(links_range) - 1
end = links_range[list_length]
current = links_range[0]
print("Initializing")
for code in links_range:
	print(1)
	code = str(code)
	uritv_video_object = uritv_video.objects.get(db_code=code)
	object_link 	= uritv_video_object.get_video_location()
	object_source 	= uritv_video_object.uri_source

	print(object_link)
	r = requests.get(object_link)
	print(2)
	if r.status_code == 403:
		print("S3 bucket does not contain video.")
		download_pending_list.append(object_source)
	else:
		uritv_video_object.s3_verified = True
		uritv_video_object.save()

log_name = "missing_videos_{}.txt".format(now)

f = open(log_name,"w+")
for missing_link in download_pending_list:
	f.write(missing_link + "\r\n")

	#add model field for s3_verified (boolean, default = False). 
	#Code to "clean_uritv" then only has to pull objects with s3_verified == 'False' rather than running the ping for all. 
	#Verification first checks code, if resposne != 403 (or is 200?) ojbect.update(s3_verified=True)