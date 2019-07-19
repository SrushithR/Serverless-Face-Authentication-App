import os
from pprint import pprint
from botocore.errorfactory import ClientError

import boto3

client = boto3.client('rekognition')


# BUCKET_NAME = os.environ['BUCKET_NAME']

class PhotoDoesNotMeetRequirementError(Exception):
    """Error raised when either there are multiple faces in the image uploaded/image has sunglasses"""

    def __init__(self, message):
        self.message = message


def lambda_handler(event, context):
    """
        Entry function in AWS Lambda
    :param event: input to the lambda function
    :return: face details detected using AWS Rekognition
    """
    file_name = event['file_name']
    try:
        response = client.detect_faces(
            Image={
                'S3Object': {
                    'Bucket': 'sheeba-cloning',
                    'Name': file_name
                }
            },
            Attributes=['ALL']
        )
    except ClientError as exception:
        print(exception)
        if type(exception).__name__ == 'InvalidImageFormatException':
            message = 'Invalid image format'
            print('Invalid image format')
        elif type(exception).__name__ == 'ImageTooLargeException':
            message = 'Image uploaded too large'
            print('Image uploaded too large')
            message = 'Image uploaded too large'
        raise PhotoDoesNotMeetRequirementError(message)
    else:
        face_details = response['FaceDetails']
        if len(face_details) != 1:
            raise PhotoDoesNotMeetRequirementError
        elif face_details[0]['Sunglasses']['Value']:
            message = 'User wearing sunglasses'
            raise PhotoDoesNotMeetRequirementError(message)
        # remove some fields not used in further processing to de-clutter the output.
        face_details[0].pop('Landmarks')
    return face_details


if __name__ == '__main__':
    event = {
        'file_name': 'scarlett.jpg'
    }
    pprint(lambda_handler(event, ''))
