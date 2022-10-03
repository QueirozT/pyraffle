from pyraffle.raffle_cli import cli
from click.testing import CliRunner

def test_cli_draft_repeat_winners_exit_code_return_0():
    runner = CliRunner()
    names_path = (
        '/home/raulin0/Documentos/projetos/pyraffle/tests/name_list.txt'
    )
    result = runner.invoke(cli, [names_path], input='2')

    assert result.exit_code == 0

def test_cli_draft_unique_winners_exit_code_return_0():
    runner = CliRunner()
    names_path = (
        '/home/raulin0/Documentos/projetos/pyraffle/tests/name_list.txt'
    )
    result = runner.invoke(cli, ['-u', names_path], input='2')

    assert result.exit_code == 0