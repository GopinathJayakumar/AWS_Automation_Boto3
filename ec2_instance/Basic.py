import os
import boto3

print('This script will help you to start or stop ec2 instances based on your required region and instance id')
ec2_con_re = boto3.resource(service_name="ec2", region_name="ap-south-1")

for each in ec2_con_re.instances.all():
    print(each.id)