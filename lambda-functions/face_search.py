import boto3
import os


class FaceAlreadyExistsError(Exception):
    """Error raised when either there are multiple faces in the image uploaded/image has sunglasses"""

    def __init__(self, message):
        self.message = message


def lambda_handler(event, context):
    """

    :param event:
    :param context:
    :return:
    """
    client = boto3.client('rekognition', region_name='us-west-2')
    # collection_id = os.environ['collection_id']
    # bucket_name = os.environ['bucket_name']
    response = client.search_faces_by_image(
        CollectionId='rider-photos',
        Image={
            'S3Object': {
                'Bucket': 'rekognition-meetup',
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
        'file_name': 'scarlett.jpg'
    }
    print(lambda_handler(event, ''))
