"""
    Mock lambda function to send failure notification back to the user
"""


def lambda_handler(event, context):
    print('input to lambda: ', event)
    # returning back the error info from the input
    return event['errorInfo']
