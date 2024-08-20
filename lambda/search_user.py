import json
import boto3
 
def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('UserTable')
    
    query_params = event['queryStringParameters']
    filter_expression = None
    expression_attribute_values = {}

    if 'Skills' in query_params:
        filter_expression = "contains(Skills, :skill)"
        expression_attribute_values[':skill'] = query_params['Skills']
    
    if 'Company' in query_params:
        filter_expression = "Company = :company"
        expression_attribute_values[':company'] = query_params['Company']
    
    if 'Domain' in query_params:
        filter_expression = "Domain = :domain"
        expression_attribute_values[':domain'] = query_params['Domain']
    
    response = table.scan(
        FilterExpression=filter_expression,
        ExpressionAttributeValues=expression_attribute_values
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(response['Items'])
    }
