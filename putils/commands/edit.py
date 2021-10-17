"""
This command combines the actions of search and put, allowing
a better way to edit parameters even if the full hierarchy is not
known.
"""
import click
from putils.cli import pass_environment
from putils.utilities import get_parameters


@click.command()
@click.argument("pattern")
@click.option(
    "-k",
    "--key",
    type=click.Choice(["Name", "Type", "Path", "Tier"], case_sensitive=True),
    default="Name",
    help="The key property to use for searching.",
)
@pass_environment
def cli(ctx, pattern, key):
    """
    Search for a particular parameter and then edit the value of it.
    """
    ssm = ctx.ssm
    parameter_list = get_parameters(
        ssm.describe_parameters,
        ParameterFilters=[{"Key": key, "Option": "Contains", "Values": [pattern]}],
    )
    if not parameter_list:
        click.echo("No parameters were found for that pattern")
        return

    for i, param in enumerate(parameter_list):
        name = param["Name"]
        click.echo(f"{i + 1}. {name}")

    click.echo()
    try:
        option = click.prompt(
            "Type the index of the parameter that you want to edit", type=int
        )
        parameter = parameter_list[option - 1]["Name"]
        ssm_get = ctx.ssm.get_parameter
        ssm_put = ctx.ssm.put_parameter
        put_kwargs = {"Name": parameter, "Type": "String", "DataType": "text"}
        parameter_check = ssm_get(Name=parameter)
        value = parameter_check["Parameter"]["Value"]
        value = click.edit(value)
        if value:
            put_kwargs["Overwrite"] = True
            put_kwargs["Value"] = value
            ssm_put(**put_kwargs)
            click.secho("Parameter edited!", fg="green", bold=True)
        else:
            click.echo("Parameter unchanged")
    except IndexError:
        click.echo("Option unvalid. Please try again with a valid parameter index.")
