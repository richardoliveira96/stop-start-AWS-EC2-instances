import json
import boto3

def lambda_handler(event, context):
    region = "us-east-1"
    EC2_RESOURCE = boto3.resource('ec2', region_name=region)
    INSTANCE_NAME_TAG_VALUE = 'DevOps'

    instancesTag = EC2_RESOURCE.instances.filter(
        Filters=[
            {
                'Name': 'tag:Group',
                'Values': [
                INSTANCE_NAME_TAG_VALUE
                ]
            }
        ]
    )

    for instance in instancesTag:
            try:
                instance.stop()
                #print(f'Starting EC2 instance: {instance.id}')
                #instance.wait_until_stopped()
                #print(f'EC2 instance "{instance.id}" has been started')
                print('Parou')
            except:
                print(f'Error stopping {instance}')
