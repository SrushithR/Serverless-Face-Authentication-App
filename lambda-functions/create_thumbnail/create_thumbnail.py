from PIL import Image
import boto3


def lambda_handler(event, context):
    """
        Entry function
    :param event: input to the lambda function
    """
    # default thumbnail size
    sizes = (250, 250)
    file_name = event['file_name']
    thumbnail_name = f"./thumbnail_{file_name}"

    client = boto3.client('s3')
    with open(f'./{file_name}', 'wb') as data:
        client.download_fileobj('rekognition-meetup', file_name, data)

    im = Image.open(file_name)
    im.thumbnail(sizes)
    im.save(thumbnail_name)

    with open(thumbnail_name, 'rb') as data:
        client.upload_fileobj(data, 'rekognition-meetup', f'thumbnail_{file_name}')


if __name__ == '__main__':
    event = {
        "file_name": "scarlett.jpg"
    }
    lambda_handler(event, '')
