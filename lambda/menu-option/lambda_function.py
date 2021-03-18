import boto3
import os
import json
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):

 customerTable = os.environ['customerTable']
 policiesTable = os.environ['policiesTable']
    
 customer_phone = event['Details']['ContactData']['CustomerEndpoint']['Address']
    
 dynamodb = boto3.resource('dynamodb')

 customerTable = dynamodb.Table(customerTable)
 policiesTable = dynamodb.Table(policiesTable)
    
 customer_query = customerTable.get_item(Key={'clientID':customer_phone})
 customer_response = customer_query['Item']
 
 responseText = []
 
 for idx, item in enumerate(customer_response['clientPolicies']):
  responseText.append(' For '+item+' insurance, press '+str(idx+1)+'.')
 responseText.append(' To hear this message again, press star now')
 menuText = ''.join(responseText)

 data = '{"ClientID": "'+customer_response['clientID']+'", \
    "Menu": "'+menuText+'", \
    "ClientName": "'+customer_response['clientName']+'"}'

 json_data = json.loads(data)
    
 return json_data