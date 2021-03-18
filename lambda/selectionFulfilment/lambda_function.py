import boto3
import os
import json

def lambda_handler(event, context):
   customerTable = os.environ['customerTable']
   policiesTable = os.environ['policiesTable']
    
   customer_phone = event['Details']['ContactData']['CustomerEndpoint']['Address']
      
   dynamodb = boto3.resource('dynamodb')

   customerTable = dynamodb.Table(customerTable)
   policiesTable = dynamodb.Table(policiesTable)
      
   customer_query = customerTable.get_item(Key={'clientID':customer_phone})
   customer_response = customer_query['Item']

   menuOption = event['Details']['Parameters']['menuOption']

   menu_query = policiesTable.get_item(Key={'policyID':customer_response['clientPolicies'][int(menuOption)-1]})
   menu_response = menu_query['Item']
   
   return {
      'menuOptionText': menu_response['description']
   }

