import json

def lambda_handler(event, context):
    print("hoga bhai mere")
    return {
        'statusCode': 200,
        'body': json.dumps('Auto-deploy test - success!')
    }