import boto3

s3 = boto3.client('s3')
s3.download_file('gopipywal1', 'Sample.txt', r'/Users/gopinathjayakumar/Desktop/Sample123.txt')