import boto3
session=boto3.Session()
ec2=session.client("ec2")
s3=session.client("s3")
rds=session.client("rds")
def list_ec2_instances():
   
    try:
        response=ec2.describe_instances()
        if not response ["Reservations"]:
            print("there are no running instances")
        else:
          for reservation in response ["Reservations"]:
           for instance in reservation ["Instances"]:
             print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}, Type: {instance['InstanceType']}, Launch Time: {instance['LaunchTime']}")
    except Exception as e:
        print(f"error occured in listing ec2_instances as {e}")
def list_s3_buckets():
    try:
     response=s3.list_buckets()
     if not response ["Buckets"]:
        print("no s3 buckets ")
     else:
        for bucket in response ["Buckets"]:
           print(f"Bucket Name: {bucket['Name']}, Creation Date: {bucket['CreationDate']}")
    except Exception as e:
       print(f"error occured in listing buckets {e}")
def describe_rds_instances():
    try:
      response=rds.describe_db_instances()
      if not response ["DBInstances"]:
         print("no rds instances ")
      else:
         for db_instance in response ["DBInstances"]:
            print(f"DB Instance Identifier: {db_instance['DBInstanceIdentifier']}, DB Instance Class: {db_instance['DBInstanceClass']}, Engine: {db_instance['Engine']}, Status: {db_instance['DBInstanceStatus']}")
    except Exception as e:
       print(f"error occured as {e}")

              
        

list_ec2_instances()
list_s3_buckets()
describe_rds_instances()