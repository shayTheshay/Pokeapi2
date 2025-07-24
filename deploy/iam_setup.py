import boto3
import json
import time
from constants import role_name, profile_name

iam = boto3.resource('iam')

def create_iam_role() -> None:
    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "ec2.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }

    try:
        iam.create_role(
            Role_name = role_name,
            AssumeRolePolicyDocument=json.dumps(trust_policy),
            Description="Role for EC2 to access dynamoDB"
        )
        print("IAM Role created")
    except iam.exeptions.EntityAlreadyExistsExeption:
        print("IAM Already exists")
    except Exception as e:
        print("Problem occured:", e)
    