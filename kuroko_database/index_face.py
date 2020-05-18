import boto3
from decimal import Decimal
import json
import urllib
import os
import boto3
import io
from PIL import Image
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kuroko_database.settings")
from django.conf import settings
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from face_index.models import face_instance, individual_instance



#-----------Variables --------------------------------------
import_files_directory_list = []
import_objects = import_files_directory_list
dynamodb = boto3.client('dynamodb')
s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')
collection  = "kuroko_django" 
bucket      = "kuroko-verified"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\kuroko_database'
path = BASE_DIR + '\\index_test'
file_type = 'jpeg'

#--------Build name / location directory list---------------

entries = os.listdir(path)

def index_face(bucket, key):

    response = rekognition.index_faces(
        Image={"S3Object":
            {"Bucket": bucket,
            "Name": key}},
            CollectionId=collection)
    return response
    
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

for file in import_files_directory_list:
    file_formal = path + '\\' + file[0]
    image = Image.open(file_formal)
    stream = io.BytesIO()
    image.save(stream,format=file_type)
    image_binary = stream.getvalue()



'''
    response = rekognition.search_faces_by_image(
            CollectionId='collection-kuroko-verified',
            Image={'Bytes':image_binary}                                       
            )

for match in response['FaceMatches']:
    if match['Similarity'] >= 80:
        print (match['Face']['FaceId'], match['Similarity'])

'''

'''



#--------Import Objects -------------------------------------
def index_faces(bucket, key):
    
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
'''