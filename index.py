import boto3
import json
from time import sleep
import sys
import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    
    #Get account ID from event 
    result = json.loads(event['body'])
    
    target_bucket = result['targetbucket']
    devops_bucket = 'gehc-devops-accounts-keys'
    
    
    logger.info('Target Bucket :' + target_bucket)
    logger.info('Secops Bucket :' + devops_bucket)
    
    try:
        s3_resource = boto3.client('s3')
        s3 = boto3.resource('s3')
        for key in s3_resource.list_objects(Bucket=target_bucket)['Contents']:
            keyfile = key['Key']
            print(keyfile)
            copy_source = {'Bucket': target_bucket ,'Key': keyfile}
            response = s3.meta.client.copy(copy_source, devops_bucket, keyfile)
            #response = s3.copy_object(Bucket= target_bucket, Key=keyfile, CopySource=copy_source, ServerSideEncryption='AES256') 
            print(response)
    except Exception as ex:
        print("Error : " + str(ex))
        return { 
                 'statusCode': 400,
                 'body': json.dumps('Failed')
               }
    return { 
             'statusCode': 200,
             'body': json.dumps('Success')
            }    
