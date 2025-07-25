import json

def lambda_handler(event, context):
    # TODO implement
    print("This is 2nd file ratan")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
