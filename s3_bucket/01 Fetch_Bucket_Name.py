
import boto3

# s3_obj = boto3.resource('s3', aws_access_key_id="", aws_secret_access_key="")
s3_obj = boto3.resource('s3')
print(type(s3_obj))
# list out all buckets - using resource
for each_bucket in s3_obj.buckets.all():
    print(each_bucket.name)
print("*"*20)

# list out all buckets - using client
s3_obj = boto3.client('s3')
response = s3_obj.list_buckets()
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')