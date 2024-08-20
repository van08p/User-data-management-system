import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('UserTable')
    
    data = json.loads(event['body'])
    
    response = table.put_item(
        Item={
            'UserID': data['UserID'],
            'Name': data['Name'],
            'Skills': data['Skills'],
            'Company': data['Company'],
            'Domain': data['Domain']
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('User added successfully!')
    }
