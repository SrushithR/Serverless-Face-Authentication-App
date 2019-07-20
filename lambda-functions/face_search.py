import boto3
import os

IMAGE_BUCKET_NAME = os.environ['IMAGE_BUCKET_NAME']


class FaceAlreadyExistsError(Exception):
    """Error raised when either there are multiple faces in the image uploaded/image has sunglasses"""

    def __init__(self, message):
        self.message = message


def lambda_handler(event, context):
    """
        Function to do a face search in the Rekognition collection
    :param event: input to the lambda function
    :return: 200 if the input image is a new face
        raises FaceAlreadyExistsError if the image is already present in the collection
    """
    client = boto3.client('rekognition')
    collection_id = event['collection_id']
    response = client.search_faces_by_image(
        CollectionId=collection_id,
        Image={
            'S3Object': {
                'Bucket': IMAGE_BUCKET_NAME,
                'Name': event['file_name'],
            }
        },
        MaxFaces=3,
        FaceMatchThreshold=70.0
    )
    number_of_matched_faces = response['FaceMatches']
    if len(number_of_matched_faces) > 0:
        message = 'Duplicate face found!'
        raise FaceAlreadyExistsError(message)
    else:
        return 200


if __name__ == '__main__':
    event = {
        "file_name": "scarlett.jpg",
        "collection_id": "<REPLACE WITH THE COLLECTION ID CREATED>"
    }
    print(lambda_handler(event, ''))
