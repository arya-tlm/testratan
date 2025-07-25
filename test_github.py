import json

def lambda_handler(event, context):
    print("Testing auto-deployment from PyCharm!")
    return {
        'statusCode': 200,
        'body': json.dumps('Auto-deploy test - success!')
    }