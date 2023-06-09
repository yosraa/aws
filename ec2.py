# créer une instance 
import boto3  

ec2 = build_aws_client("s3")
response = ec2.describe_instances()
print(response)
# run_instances lance le nombre spécifié d'instances à l'aide d'un AMI pour lequel vous disposez des autorisation.
conn = ec2.run_instances(ImageId='<ami-image-id>',
                         InstanceType="t2.micro",
                         MaxCount=5,
                         MinCount=1
                        )
                         
