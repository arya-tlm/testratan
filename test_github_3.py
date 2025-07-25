import json

def lambda_handler(event, context):
    # TODO implement
    print("THis is 3rd file")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
