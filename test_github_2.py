import json

def lambda_handler(event, context):
    # TODO implement
    print("This is 2nd file")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
