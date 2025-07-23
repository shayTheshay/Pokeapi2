import boto3
import os
from botocore.exceptions import ClientError
from dotenv import load_dotenv 
load_dotenv()

def deploy_dynamoDB() -> None:
    try:
        create_dynamoDB_instance()
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceInUseException':
            print("DynamoDB table already exists. Skipping creation.")
        else:
            print("PROBLEM OCCURED! BAD CREATION FOR DYNAMODB", e.repose['Error']['Code'],e.response['Error']['Message'])

def create_dynamoDB_instance() -> None:
   # Create a DynamoDB client using the default credentials and region
    dynamodb = boto3.resource('dynamodb', region_name = os.getenv("REGION_NAME"))

    #Create the DynamoDB table.
    table = dynamodb.create_table(
        TableName=os.getenv("DYNAMODB_NAME"),
        KeySchema=[
            {'AttributeName': 'id', 'KeyType': 'HASH'}
        ],
        AttributeDefinitions=[
            {'AttributeName': 'id', 'AttributeType': 'N'}
        ], BillingMode='PAY_PER_REQUEST'
        
    )
    table.wait_until_exists()
 