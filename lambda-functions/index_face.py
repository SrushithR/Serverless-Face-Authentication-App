import boto3


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
    client = boto3.client('rekognition', region_name='us-west-2')
    response = client.index_faces(
        CollectionId='rider-photos',
        Image={
            'S3Object': {
                'Bucket': 'rekognition-meetup',
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
        'file_name': 'scarlett.jpg',
        'user_id': 'Scarlett'
    }
    print(lambda_handler(event, ''))
