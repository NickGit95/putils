"""
This command manages deletion of parameters.
"""
import click
from botocore.exceptions import ClientError
from putils.cli import pass_environment


@click.command()
@click.argument("param")
@pass_environment
def cli(ctx, param):
    """
    Delete a parameter hierachy.
    """
    ssm = ctx.ssm
    try:
        response = ssm.delete_parameter(Name=param)
        click.secho("Parameter successfully deleted!", fg="green", bold=True)
    except ClientError as exception:
        if exception.response["Error"]["Code"] == "ParameterNotFound":
            click.secho("Parameter not found!", fg="red")
