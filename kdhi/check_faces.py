import boto3
from decimal import Decimal
import json
import urllib
import os
import boto3
import io
from PIL import Image
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kdhi.settings")
from django.conf import settings
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from kuroko.models import face, figure



#-----------Variables --------------------------------------
import_files_directory_list = []
import_objects = import_files_directory_list
dynamodb = boto3.client('dynamodb')
s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')
collection  = "kdhi_collection" 
bucket      = "kuroko-verified"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\kdhi\\kuroko'
path = BASE_DIR + '\\index'
file_type = 'jpeg'

#--------Build name / location directory list---------------

entries = os.listdir(path)
client = boto3.client('s3')
response_list = client.list_objects(
    Bucket=bucket,
)
for response in response_list['Contents']:
	response_contents = response['Key']
	print(response_contents)