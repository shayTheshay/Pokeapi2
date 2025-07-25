import boto3
import os
from dotenv import load_dotenv 
from .security_group_setup import get_security_group_id

load_dotenv()

def ec2_deploy() -> None:
    ec2 = boto3.resource('ec2', region_name=os.getenv("REGION_NAME"))

    filters = [
        {'Name': 'tag:Name', 'Values': [os.getenv("POKEMON_EC2_NAME")]},
        {'Name': 'instance-state-name', 'Values': ['pending', 'running', 'stopped']}
    ]

    instances = list(ec2.instances.filter(Filters=filters))
    for instance in instances:
        name_tag = next((tag['Value'] for tag in instance.tags if tag['Key'] == 'Name'), None)
        if name_tag == os.getenv("POKEMON_EC2_NAME"):            
            if instance.state['Name'] == 'stopped':
                instance.start()
                instance.wait_until_running()
                instance.reload()
            return
    print("No instance found, creating a new instance")        
    create_instance()



def create_instance() -> None:

    sg_id = get_security_group_id()
    ec2 = boto3.resource('ec2', region_name=os.getenv("REGION-NAME"))
    instance = ec2.create_instances(
        ImageId=os.getenv("IMAGE_ID"),  # Replace with Ubuntu AMI
        MinCount=1,
        MaxCount=1,
        InstanceType=os.getenv("INSTANCE_TYPE"),
        KeyName=os.getenv("KEY_PAIR_NAME"),
        SecurityGroupIds=[sg_id],  # Open port 22 and 8000
        UserData=open('deploy/setup_script.sh').read(),   # We'll define this below
        TagSpecifications=[{
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': os.getenv("POKEMON_EC2_NAME")}]
        }],
        IamInstanceProfile={'Name': 'LabInstanceProfile'}
    )[0]
    print("Launched:", instance.id)

    