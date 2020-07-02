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
collection  = "kuroko_django" 
bucket      = "kuroko-verified"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\kuroko_database'
path = BASE_DIR + '\\index'
file_type = 'jpeg'

#--------Build name / location directory list---------------

entries = os.listdir(path)


def format_file_name(file):
    temp_file_list = []
    file_name = file.split('.')[0]
    try:
        file_name = file_name.split('(')[0]
    except:
        pass
    temp_file_list = [file, file_name]
    import_files_directory_list.append(temp_file_list)

for file in entries:
    format_file_name(file)


#----------SEARCH FACE
'''
for file in import_files_directory_list:
    file_formal = path + '\\' + file[0]
    image = Image.open(file_formal)
    stream = io.BytesIO()
    image.save(stream,format=file_type)
    image_binary = stream.getvalue()
    search_response = rekognition.search_faces_by_image(
            CollectionId='kdhi_kuroko_collection',
            Image={'Bytes':image_binary})    
    for match in search_response['FaceMatches']:
        matches_list = {0 : 'Null'}
        similarity_list = []
        if match['Similarity'] >= 80:
            similary = match['Similarity']
            kuroko_id = str(match['Face']['FaceId'])
            face_instance_object = face_instance.objects.get(kuroko_id=kuroko_id)
            linked_individual = face_instance_object.individual_match.name

            similarity_list.append(similary)
            matches_list[similary]  = linked_individual
        top_result = max(similarity_list)
        top_result_individual = matches_list.get(top_result)
        print("Top result = {}".format(top_result_individual) )
        print("Similary was {}".format(top_result))
'''     

#--------------INDEX FACE 
def index_face(bucket, key):

    response = rekognition.index_faces(
        Image={"S3Object":
            {"Bucket": bucket,
            "Name": key}},
            CollectionId=collection)
    return response


#index_toggle    = input("Index this face? [y/n]")
#create_toggle   = input("Link to {}? [y/n]".format(top_result_individual))

index_toggle = 'y'
if index_toggle == 'y':

    for import_object in import_files_directory_list:
        key = import_object[0]
        individual_instance_name = import_object[1]
        print(key)
        response = index_face(bucket, key)

        #-------CREATE INDIVIDUAL INSTANCE (second version replace this if/then to link to existing face based on search result)
        # this should go second in later versions, for now just needed to create individuals as current db is empty
        individual = individual_instance(name=individual_instance_name)
        individual.save()

        #-------CREATE FACE INSTANCE
        kuroko_id = response['FaceRecords'][0]['Face']['FaceId']
        face = face(
            name=kuroko_id, 
            image_filename=key,
            )
        face.save()


#------------UPDATE INDEXES
# make script that goes through all faces, pulls associated individual, and then appends face's kuroko_id to individual_instance's face list