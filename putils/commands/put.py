"""
This command manages creation of new parameters.
If a parameter already exists, the user can edit its value
and then update it.
"""
import click
from botocore.exceptions import ClientError
from putils.cli import pass_environment


@click.command()
@click.argument("param")
@pass_environment
def cli(ctx, param):
    """
    Create a new parameter or overwrite an existing one.
    """
    ssm_get = ctx.ssm.get_parameter
    ssm_put = ctx.ssm.put_parameter
    put_kwargs = {"Name": param, "Type": "String", "DataType": "text"}
    try:
        parameter_check = ssm_get(Name=param)
        click.echo("Parameter already exists")
        click.echo("Do you want to edit it? [yn] ", nl=False)
        click.echo()
        char = click.getchar()
        if char == "y":
            value = parameter_check["Parameter"]["Value"]
            value = click.edit(value)
            if value:
                put_kwargs["Overwrite"] = True
                put_kwargs["Value"] = value
                ssm_put(**put_kwargs)
                click.secho("Parameter edited!", fg="green", bold=True)
            else:
                click.echo("Parameter unchanged")
                return
    except ClientError as exception:
        if exception.response["Error"]["Code"] == "ParameterNotFound":
            value = click.edit("")
            if value:
                put_kwargs["Overwrite"] = False
                put_kwargs["Value"] = value
                put_kwargs["Tier"] = "Standard"
                ssm_put(**put_kwargs)
                click.secho("Parameter Added!", fg="green", bold=True)
            else:
                click.echo("Parameter not created")
