import boto3
import os
import random
import json

dynamodb = boto3.resource('dynamodb')
# We put DynamoDB table name in lambda environment variables and reference here because table name changes with different environment.
#DYNAMODB_TABLE_NAME is key for env. variable and value is table name.
table = dynamodb.Table(os.environ['DYNAMODB_TABLE_NAME'])

def lambda_handler(event, context):

    try:
        for record in event['Records']:
            body = json.loads(record["body"])
            print(body)

            eid = body['employeeid']
            ename = body['employeename']
            eage = body['employeeage']
            edesignation = body['employeedesignation']

            response = table.put_item(
                Item={
                    "employeeid": eid,
                    "employeename": ename,
                    "employeeage": eage,
                    "employeedesignation": edesignation
                }
            )
            print(response)

    except Exception as e:
        print(e)
        raise e
