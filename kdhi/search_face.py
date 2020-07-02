
import boto3
import io
from PIL import Image
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kdhi.settings")
from django.conf import settings
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from kuroko.models import face, figure

rekognition = boto3.client('rekognition', region_name='us-east-1')
dynamodb = boto3.client('dynamodb', region_name='us-east-1')
collection  = "kdhi_collection" 
bucket      = "kuroko-verified"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\kdhi\\kuroko'
path = BASE_DIR + '\\test\\'


entries = os.listdir(path)
for file in entries:
	file_type = file.split(".")[1]
	if file_type == 'jpg':
		file_type = 'jpeg'
	file_abs = path + file 
	image = Image.open(file_abs)
	stream = io.BytesIO()
	image.save(stream,format=file_type)
	image_binary = stream.getvalue()
	response = rekognition.search_faces_by_image(
		CollectionId=collection,
		Image={'Bytes':image_binary}                                       
		)

	for match in response['FaceMatches']:
		if match['Similarity'] >= 80:
			match_face_id 		= match['Face']['FaceId']
			match_similarity 	= match['Similarity']
			match_face_object 	= face.objects.get(name=match_face_id) 
			try:
				figure_match = match_face_object.verified_figure
				match_touple = [figure_match, match_similarity]
			except:
				print("Matched face lacks a verified figure link, face code is: {}".format(match_face_id))
				match_touple = [match_face_id, match_similarity]
			print(match_touple)