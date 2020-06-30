
import bs4
import requests
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
end = 36010
download_pending_list = []
links_range = range(current, end)
code_count = 0
for code in links_range:
	code = str(code)
	uritv_video_object = uritv_video.objects.get(db_code=code)
	object_link 	= uritv_video_object.get_video_location()
	object_source 	= uritv_video_object.uri_source

	r = requests.get(object_link)
	if r.status_code == 403:
		print("S3 bucket does not contain video.")
		download_pending_list.append(object_source)

log_name = "missing_videos_{}_to_{}.txt".format(current, end)

f = open(log_name,"w+")
for missing_link in download_pending_list:
	f.write(missing_link + "\r\n")

	#add model field for s3_verified (boolean, default = False). 
	#Code to "clean_uritv" then only has to pull objects with s3_verified == 'False' rather than running the ping for all. 
	#Verification first checks code, if resposne != 403 (or is 200?) ojbect.update(s3_verified=True)