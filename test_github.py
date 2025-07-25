import json

def lambda_handler(event, context):
    print("hoga bhai mere ab sbka hoga")
    return {
        'statusCode': 200,
        'body': json.dumps('Auto-deploy test - success!')
    }