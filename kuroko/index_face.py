import boto3
from decimal import Decimal
import json
import urllib


import_files_directory_list = []
import_objects = import_files_directory_list
dynamodb = boto3.client('dynamodb')
s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')
collection  = "faces_set" 
bucket      = "kuroko.faces"
path = 'D:\\Sam\\kurko.faces\\import_pending'


for import_object in import_files_directory_list:


def index_faces(bucket, key):

    response = rekognition.index_faces(
        Image={"S3Object":
            {"Bucket": bucket,
            "Name": key}},
            CollectionId=collection)
    return response

for items in import_object:
    response = index_faces(bucket, items[0])
    faceId = response['FaceRecords'][0]['Face']['FaceId']
    print(faceID)
