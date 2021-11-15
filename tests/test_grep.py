from click.testing import CliRunner


def test_grep_full(init_params):
    """Test the full output without options"""
    from putils.cli import cli

    runner = CliRunner()
    response = runner.invoke(cli, ["grep", "/dev/", "ipsum"], color=False)
    assert response.output == "/dev/test3\nLorem ipsum\n/dev/test4\nipsum testing\n"


def test_grep_only_names(init_params):
    """Test the in output with the option -l"""
    from putils.cli import cli

    runner = CliRunner()
    response = runner.invoke(cli, ["grep", "-l", "/dev/", "ipsum"], color=False)
    assert response.output == "/dev/test3\n/dev/test4\n"
