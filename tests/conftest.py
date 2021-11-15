from moto import mock_ssm
import boto3
import os
import pytest


@pytest.fixture(scope="module")
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "us-east-2"
    os.environ["EDITOR"] = "vim"


@pytest.fixture(scope="module")
def ssm(aws_credentials):
    with mock_ssm():
        yield boto3.client("ssm")


@pytest.fixture(scope="module")
def init_params(ssm):
    param_list = [
        {
            "Name": "test",
            "Description": "name",
            "Value": "testing",
            "Type": "String",
            "Overwrite": True,
            "Tier": "Standard",
            "DataType": "text",
        },
        {
            "Name": "test2",
            "Description": "name",
            "Value": "testing",
            "Type": "String",
            "Overwrite": True,
            "Tier": "Standard",
            "DataType": "text",
        },
        {
            "Name": "/dev/test3",
            "Description": "name",
            "Value": "Lorem ipsum",
            "Type": "String",
            "Overwrite": True,
            "Tier": "Standard",
            "DataType": "text",
        },
        {
            "Name": "/dev/test4",
            "Description": "name",
            "Value": "ipsum testing",
            "Type": "String",
            "Overwrite": True,
            "Tier": "Standard",
            "DataType": "text",
        },
        {
            "Name": "/dev/Delete",
            "Description": "name",
            "Value": "Delete this",
            "Type": "String",
            "Overwrite": True,
            "Tier": "Standard",
            "DataType": "text",
        },
        {
            "Name": "param1",
            "Description": "name",
            "Value": "Example",
            "Type": "String",
            "Overwrite": True,
            "Tier": "Standard",
            "DataType": "text",
        },
        {
            "Name": "param2",
            "Description": "name",
            "Value": "Example",
            "Type": "String",
            "Overwrite": True,
            "Tier": "Standard",
            "DataType": "text",
        },
        {
            "Name": "param3",
            "Description": "name",
            "Value": "Example",
            "Type": "String",
            "Overwrite": True,
            "Tier": "Standard",
            "DataType": "text",
        },
        {
            "Name": "param4",
            "Description": "name",
            "Value": "Example",
            "Type": "String",
            "Overwrite": True,
            "Tier": "Standard",
            "DataType": "text",
        },
        {
            "Name": "param5",
            "Description": "name",
            "Value": "Example",
            "Type": "String",
            "Overwrite": True,
            "Tier": "Standard",
            "DataType": "text",
        },
        {
            "Name": "param6",
            "Description": "name",
            "Value": "Example",
            "Type": "String",
            "Overwrite": True,
            "Tier": "Standard",
            "DataType": "text",
        },
    ]
    for param in param_list:
        ssm.put_parameter(**param)
    return ssm
