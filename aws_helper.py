import os

import boto3

import config_by_name


def build_aws_client(aws_service):
    if os.getenv("PLATFORM", "local") == "local":
        session = boto3.Session(profile_name="local")
        return session.client(aws_service, **config_by_name[os.getenv("PLATFORM", "local")].AWS_EXTRA_PARAMETERS)
    if os.getenv("AWS_REGION"):
        return boto3.client(aws_service, region_name=os.getenv("AWS_REGION"))
    return None
