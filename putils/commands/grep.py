"""
This command is similar to GNU grep but for parameter store.
"""
import re
import click
from putils.cli import pass_environment
from putils.utilities import get_parameters


@click.command()
@click.option(
    "-l",
    "--files-with-matches",
    flag_value=False,
    default=True,
    help="Only show the parameter names and not the matched lines.",
)
@click.argument("path")
@click.argument("pattern")
@pass_environment
def cli(ctx, path, pattern, files_with_matches):
    """
    Search for matches on the parameter values from a hierarchy path.
    """
    ssm = ctx.ssm
    parameter_list = get_parameters(
        ssm.get_parameters_by_path,
        Path=path,
        Recursive=True,
        WithDecryption=True,
        MaxResults=10,
    )
    for param in parameter_list:
        value = param["Value"]
        matches = re.findall(r".*{}.*".format(pattern), value)
        if len(matches) > 0:
            click.secho(param["Name"], bold=True, fg="green")
            if files_with_matches:
                for match in matches:
                    color_result = re.sub(
                        pattern, lambda m: click.style(m.group(), fg="red"), match
                    )
                    click.echo(color_result)
