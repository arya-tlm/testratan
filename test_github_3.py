import json

def lambda_handler(event, context):
    # TODO implement
    print("mera bhi hogya bhai")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
