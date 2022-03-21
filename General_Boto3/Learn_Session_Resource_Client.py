# session - Fetch iam username list
import boto3

session = boto3.session.Session(profile_name="default")
iam_dashboard =  session.resource(service_name="iam", region_name="ap-south-1")

for each_user in iam_dashboard.users.all():
    print(each_user.name)
print("*"*10)
#*************************************************************************************************************
# Client - Fetch iam username list
session = boto3.session.Session(profile_name="default")
iam_dashboard =  session.client(service_name="iam", region_name="ap-south-1")

for each_user in iam_dashboard.list_users()['Users']:
    print(each_user['UserName'])
print("*" * 10)
#*************************************************************************************************************
# meta - Fetch iam username list
session = boto3.session.Session(profile_name="default")
iam_dashboard =  session.resource(service_name="iam", region_name="ap-south-1")

for each_user in iam_dashboard.meta.client.list_users()['Users']:
    print(each_user['UserName'])
print("*" * 10)
#*************************************************************************************************************