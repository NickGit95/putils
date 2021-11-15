from click.testing import CliRunner


def test_search(init_params):
    from putils.cli import cli

    runner = CliRunner()
    response = runner.invoke(cli, ["search", "test"])
    assert response.output == "test\ntest2\n/dev/test3\n/dev/test4\n"
