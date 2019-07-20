"""
    Lambda Function to create a thumbnail for the input image and upload it to S3
"""

import os

from PIL import Image
import boto3

IMAGE_BUCKET_NAME = os.environ['IMAGE_BUCKET_NAME']
THUMBNAIL_BUCKET_NAME = os.environ['THUMBNAIL_BUCKET_NAME']


def lambda_handler(event, context):
    """
        Function to create a thumbnail for the input image and upload it to S3
    :param event: input to the lambda function
    """
    # default thumbnail size
    sizes = (250, 250)
    file_name = event['file_name']
    thumbnail_name = "/tmp/thumbnail_{}".format(file_name)

    client = boto3.client('s3')
    # downloading the file to the tmp folder
    with open('/tmp/{}'.format(file_name), 'wb') as data:
        client.download_fileobj(IMAGE_BUCKET_NAME, file_name, data)

    im = Image.open(file_name)
    im.thumbnail(sizes)
    im.save(thumbnail_name)

    with open(thumbnail_name, 'rb') as data:
        client.upload_fileobj(data, THUMBNAIL_BUCKET_NAME, 'thumbnail_{}'.format(file_name))


if __name__ == '__main__':
    event = {
        "file_name": "scarlett.jpg",
        "collection_id": "bookmycab-collection",
        "user_id": "scarlett"
    }
    lambda_handler(event, '')
