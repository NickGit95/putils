from click.testing import CliRunner


def test_delete_ok(init_params):
    """Test the full output without options"""
    from putils.cli import cli

    runner = CliRunner()
    response = runner.invoke(cli, ["delete", "/dev/Delete"])
    assert response.output == "Parameter successfully deleted!\n"


def test_delete_fail(init_params):
    """Test the full output without options"""
    from putils.cli import cli

    runner = CliRunner()
    response = runner.invoke(cli, ["delete", "/dev/param"])
    assert response.output == "Parameter not found!\n"
