import json

def lambda_handler(event, context):
    print("Hello World! hi ratan bhaiya")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
