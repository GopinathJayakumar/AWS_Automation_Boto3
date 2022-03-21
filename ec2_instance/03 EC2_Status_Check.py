import boto3

session = boto3.session.Session(profile_name="default")
ec2_console =  session.resource(service_name="ec2", region_name="ap-south-1")
instance_status = ec2_console.Instance("IAM Number")
print("Instance status is: ", instance_status.state['Name'])