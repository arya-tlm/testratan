import json

def lambda_handler(event, context):
    # TODO implement
    print("hogya bhai tension mt le")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
