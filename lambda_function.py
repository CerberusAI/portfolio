import json
import boto3    # AWS services

# Homework: develop function to send email and / or text using SNS
def send_to_SNS(Event):
    # Logs to CloudWatch
    print(json.dumps(Event))

# Entry point function
def lambda_handler(event, context):

    # Process event & send to SNS
    send_to_SNS(event)
    
    # Response JSON sent back client
    response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST'
        },
        'body': 'Roger Roger...'
    }
    
    return response
