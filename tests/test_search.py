from click.testing import CliRunner
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


@pytest.fixture(scope="module")
def ssm(aws_credentials):
    with mock_ssm():
        yield boto3.client("ssm")


def test_search(ssm):
    from putils.cli import cli

    ssm.put_parameter(
        Name="test",
        Description="name",
        Value="testing",
        Type="String",
        Overwrite=True,
        Tier="Standard",
        DataType="text",
    )
    runner = CliRunner()
    response = runner.invoke(cli, ["search", "test"])
    assert response.output == "test\n"
