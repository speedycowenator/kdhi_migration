
import boto3
import io
from PIL import Image
#D:\Dropbox\Dropbox\kdhi.org\Assets\Leadership Photos\Kuroko\test\
rekognition = boto3.client('rekognition', region_name='us-east-1')
dynamodb = boto3.client('dynamodb', region_name='us-east-1')
file_location = 'D:\\Dropbox\\Dropbox\\kdhi.org\\Assets\\Leadership Photos\\Kuroko\\test\\'    
file_name = input("Input file name without extension: ")
#file_type = input("Input extension (png or jpg): ")
file_type = "png"
image_true =file_location + file_name + '.' + file_type

if file_type == 'jpg':
    file_type = 'jpeg'


    
image = Image.open(image_true)

stream = io.BytesIO()
image.save(stream,format=file_type)
image_binary = stream.getvalue()


response = rekognition.search_faces_by_image(
        CollectionId='collection-kuroko-verified',
        Image={'Bytes':image_binary}                                       
        )
    
for match in response['FaceMatches']:
    if match['Similarity'] >= 80:
        print (match['Face']['FaceId'], match['Similarity'])
            
        face = dynamodb.get_item(
            TableName='table-kuroko-verified',  
            Key={'RekognitionId': {'S': match['Face']['FaceId']}}
            )
        
        if 'Item' in face:
            print (face['Item']['FullName']['S'])
        else:
            print ('no match found in person lookup')