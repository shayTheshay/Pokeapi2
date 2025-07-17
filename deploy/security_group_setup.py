import boto3
import os
from dotenv import load_dotenv 
load_dotenv()


def create_security_group():
    ec2 = boto3.client('ec2')

    # Get your default VPC (or specify a different one if needed)
    vpcs = ec2.describe_vpcs()
    vpc_id = vpcs['Vpcs'][0]['VpcId']

    # Create the security group
    sg_response = ec2.create_security_group(
        GroupName=os.getenv("SECURITY_GROUP_NAME"),
        Description='Allow SSH and app access',
        VpcId=vpc_id
    )
    sg_id = sg_response['GroupId']

    # Add ingress rules
    ec2.authorize_security_group_ingress(
        GroupId=sg_id,
        IpPermissions=[
            {
                'IpProtocol': 'tcp',
                'FromPort': 22,      # SSH
                'ToPort': 22,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
            },
            {
                'IpProtocol': 'tcp',
                'FromPort': 8000,    # PokeAPI port
                'ToPort': 8000,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
            }
        ]
    )
    print("Security Group created with ID:", sg_id)
    return sg_id



def get_security_group_id():
    ec2 = boto3.client('ec2')
    vpcs = ec2.describe_vpcs()
    vpc_id = vpcs['Vpcs'][0]['VpcId']

    # Check if SG already exists
    existing_groups = ec2.describe_security_groups(
        Filters=[
            {'Name': 'group-name', 'Values': ['pokeapi-sg']},
            {'Name': 'vpc-id', 'Values': [vpc_id]}
        ]
    )['SecurityGroups']

    if existing_groups:
        sg_id = existing_groups[0]['GroupId']
        print(f"Security Group already exists: {sg_id}")
        return sg_id

    # If not exists, create it
    print("Security Group does not exist. Creating it...")
    return create_security_group()