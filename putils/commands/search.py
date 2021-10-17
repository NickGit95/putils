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
    Return the names of parameters that match a certain pattern.
    """
    ssm = ctx.ssm
    parameter_list = get_parameters(
        ssm.describe_parameters,
        ParameterFilters=[{"Key": key, "Option": "Contains", "Values": [pattern]}],
    )
    for param in parameter_list:
        click.secho(param["Name"], bold=True, fg="green")
