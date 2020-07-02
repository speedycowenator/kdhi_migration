import requests
import boto3

import bs4
import requests
import csv
import time
from google.cloud import translate_v2 as translate
translator = translate.Client()
from datetime import date, timedelta

now = date.today()
import bs4
import urllib.request
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kdhi.settings")
from django.conf import settings
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from media_archive.models import uritv_video
import csv
from random import randint

s3 = boto3.client('s3')
bucket      = "uritv-bucket"

import_files_directory_list = []

paginator = s3.get_paginator('list_objects_v2')
pages = paginator.paginate(
	Bucket=bucket
	)

for page in pages:
	for response in page['Contents']:
		try:
			file        = response['Key']
			file_name   = file.split(".")[0]
			file_size   = response['Size']
			temp_file_list = [file, file_name, file_size]
			import_files_directory_list.append(file)
		except:
			pass

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

for code in links_range:
	code = str(code)
	uritv_video_object = uritv_video.objects.get(db_code=code)
	object_link 	= uritv_video_object.file_name
	object_source 	= uritv_video_object.uri_source
	if object_link in import_files_directory_list:
		print("Found, updating verification for {}.".format(code))
		uritv_video_object.s3_verified = True
		uritv_video_object.save()
	else:
		download_pending_list.append(object_source)
		
log_name = "missing_videos_{}.txt".format(end)

print(len(import_files_directory_list))
f = open(log_name,"w+")
for missing_link in download_pending_list:
	f.write(missing_link + "\r\n")
