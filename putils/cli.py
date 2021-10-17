"""Click module initialitation"""
import os
import sys
import click
from boto3 import session


CONTEXT_SETTINGS = dict(auto_envvar_prefix="PUTILS")


class Environment:
    """Environment object to pass to each command"""

    def __init__(self):
        self.verbose = False
        self.ssm = None
        self.log_color = "red"

    def log(self, msg, *args):
        """Logs a message to stderr."""
        if args:
            msg %= args
        click.echo(msg, file=sys.stderr)

    def vlog(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log(msg, *args)


pass_environment = click.make_pass_decorator(Environment, ensure=True)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))
aws_session = session.Session()


class ParamsCLI(click.MultiCommand):
    """Child class of click.MultiCommand"""

    def list_commands(self, ctx):
        command_list = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith(".py") and filename != "__init__.py":
                command_list.append(filename[:-3])
        command_list.sort()
        return command_list

    def get_command(self, ctx, cmd_name):
        try:
            mod = __import__(f"putils.commands.{cmd_name}", None, None, ["cli"])
        except ImportError:
            return
        return mod.cli


@click.command(cls=ParamsCLI, context_settings=CONTEXT_SETTINGS)
@click.option("-r", "--region", default="us-east-2", help="The AWS region to use.")
@click.option("-v", "--verbose", is_flag=True, help="Enables verbose mode.")
@pass_environment
def cli(ctx, region, verbose):
    """Various utilities to work with AWS parameter store."""
    ctx.verbose = verbose
    ctx.ssm = aws_session.client(service_name="ssm", region_name=region)
