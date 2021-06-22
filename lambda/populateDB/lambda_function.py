import json
import boto3
import os

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb')

    customerTable = os.environ['customerTable']
    table1 = dynamodb.Table(customerTable)
    
    policiesTable = os.environ['policiesTable']
    table2 = dynamodb.Table(policiesTable)
    
    # Phone numbers should follow international format E.164
    table1.put_item(
       Item={
            'clientID': '+3526919xxxxxx',
            'clientName': 'Marius',
            'clientPolicies': ['car','house']
        }
    )
    
    table1.put_item(
       Item={
            'clientID': '+3526919xxxxxx',
            'clientName': 'John',
            'clientPolicies': ['boat','pet']
        }
    )
    
    table2.put_item(
       Item={
            'policyID': 'car',
            'description': 'Your car insurance covers third party damage and theft. Authorized service points are this and that.'
        }
    )
    
    table2.put_item(
       Item={
            'policyID': 'house',
            'description': 'Your house insurance covers damage caused by natural disasters, fires and earthquakes. To fill a claim, please visit our website.'
        }
    )
    
    table2.put_item(
       Item={
            'policyID': 'boat',
            'description': 'Your boat insurance covers damage caused by natural distasters and fires. To fill a claim, please visit our website.'
        }
    )
    
    table2.put_item(
       Item={
            'policyID': 'pet',
            'description': 'Your pet insurance covers any medical interventions required to keep your pet healty. For a list of approved vet centers, please visit our website.'
        }
    )
    
    return 'ok'
