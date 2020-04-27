import boto3
from decimal import Decimal
import json
import urllib
import os

#-----------Variables --------------------------------------
import_files_directory_list = []
import_objects = import_files_directory_list
dynamodb = boto3.client('dynamodb')
s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')
collection  = "collection-kuroko-verified" 
bucket      = "kuroko-verified"
path = 'D:\\Dropbox\\Dropbox\\kdhi.org\\Assets\\Leadership Photos\\Kuroko\\verified'


#--------Build name / location directory list---------------

entries = os.listdir(path)
def index_file_name(file):
    temp_file_list = []
    file_name = file.split('.')[0]
    try:
        file_name = file_name.split('(')[0]
    except:
        pass
    temp_file_list = [file, file_name]
    import_files_directory_list.append(temp_file_list)

for file in entries:
    index_file_name(file)


#--------Import Objects -------------------------------------
def index_faces(bucket, key):

    response = rekognition.index_faces(
        Image={"S3Object":
            {"Bucket": bucket,
            "Name": key}},
            CollectionId=collection)
    return response
    
def update_index(tableName,faceId, fullName):
    response = dynamodb.put_item(
        TableName=tableName,
        Item={
            'RekognitionId': {'S': faceId},
            'FullName': {'S': fullName}
            }
        ) 


# --------------- Face Import (Rekognition and Dynamo Database) ------------------

for import_object in import_files_directory_list:
    key = import_object[0]
    personFullName = import_object[1]
    print(key)
    response = index_faces(bucket, key)
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        faceId = response['FaceRecords'][0]['Face']['FaceId']
        personFullName = import_object[1]
        update_index('table-kuroko-verified',faceId,personFullName)
        print(response)

    else:
        print("Error processing object {} from bucket {}. ".format(key, bucket))
