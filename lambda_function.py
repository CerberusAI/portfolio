import json

# Entry point function
def lambda_handler(event, context):
    
    # Logs to CloudWatch
    print(json.dumps(event['body']))
    
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
