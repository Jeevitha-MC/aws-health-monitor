#Create EC2 client

import boto3

def get_ec2_client():
    return boto3.client('ec2')

def get_cloudwatch_client():
    return boto3.client('cloudwatch')

def get_sns_client():
    return boto3.client('sns')

