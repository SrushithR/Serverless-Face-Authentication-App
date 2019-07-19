"""
    Lambda function to index the input image to the collection
"""
import os

import boto3

BUCKET_NAME = os.environ['IMAGE_BUCKET_NAME']
client = boto3.client('rekognition')


def lambda_handler(event, context):
    """
        Entry function in AWS Lambda
    :param event: input to the lambda function
        Sample input:
            event = {
                'file_name': 'scarlett.jpg',
                'user_id': 'Scarlett'
            }

    :return: indexed face details
    """

    response = client.index_faces(
        CollectionId='rider-photos',
        Image={
            'S3Object': {
                'Bucket': BUCKET_NAME,
                'Name': event['file_name'],
            }
        },
        ExternalImageId=event['user_id'],
        DetectionAttributes=[
            'DEFAULT',
        ]
    )
    return response['FaceRecords'][0]['Face']


if __name__ == '__main__':
    event = {
        "file_name": "scarlett.jpg",
        "user_id": "Scarlett"
    }
    print(lambda_handler(event, ''))
