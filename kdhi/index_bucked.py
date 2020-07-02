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
entries = os.listdir(path)


entries = os.listdir(path)
client = boto3.client('s3')
response_list = client.list_objects(
    Bucket=bucket,
)
for response in response_list['Contents']:
    file        = response['Key']
    file_name   = file.split(".")[0]
    file_size   = response['Size']
    temp_file_list = [file, file_name, file_size]
    import_files_directory_list.append(temp_file_list)

for file in entries:
    format_file_name(file)

def index_face(bucket, key):

    response = rekognition.index_faces(
        Image={"S3Object":
            {"Bucket": bucket,
            "Name": key}},
            CollectionId=collection)
    return response

index_toggle = 'y'
if index_toggle == 'y':

    for import_object in import_files_directory_list:
        key = import_object[0]
        individual_instance_name = import_object[1]
        face_size = import_object[2]
        print(key)
        response = index_face(bucket, key)

        kuroko_id = response['FaceRecords'][0]['Face']['FaceId']
        face_object = face(
            name=kuroko_id, 
            image_filename=key,
            image_quality=face_size,
            )
        face_object.save()