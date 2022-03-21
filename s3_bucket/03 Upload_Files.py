import boto3
import logging
import os
# Way 01: using resource

## s3_obj = boto3.resource('s3', aws_access_key_id="", aws_secret_access_key="")
    # s3_obj = boto3.resource('s3')
    # print(type(s3_obj))
    # upload file in to specific bucket:-
    # s3_obj.Bucket('gopipywal').put_object(Key='Sample.txt')
    # print('Uploaded')
## *****************************************************************************
from botocore.exceptions import ClientError


def upload_file(file_name, bucket, file_object=None):

    if file_object is None:
        file_object = file_name

    client = boto3.client("s3")
    try:
        response = client.upload_file(file_name, bucket, file_object)
    except ClientError as e:
        logging.error(e)
        return False
    return True

upload_file("Sample.txt", 'gopipywal1')
