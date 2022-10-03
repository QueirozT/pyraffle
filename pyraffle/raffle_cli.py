from pathlib import Path
import click
from loguru import logger
from raffle import Raffle


@click.command(help='Realize sorteios com, ou sem, vencedores repetidos')
@click.argument('names_path', type=click.Path(exists=True))
@click.option('-u', '--unique', 'unique', help='Para não repetir vencedores', is_flag=True)
def cli(names_path, unique):
    raffle = Raffle(load_names(names_path))
    logger.info(f'Os seguintes nomes foram carregados: {raffle.names_list}')
    valid_number_of_winners = False
    while not valid_number_of_winners:
        number_of_winners = click.prompt('Quantos nomes serão sorteados?', type=int)
        valid_number_of_winners = number_of_winners <= len(raffle.names_list)
        raffle.draft(valid_number_of_winners, number_of_winners, unique)


def load_names(names_path):
    with open(Path(names_path), 'r', encoding='utf-8') as names: 
        with click.progressbar(names, label='Carregando nomes para sorteio') as bar:
            names_list = [name.strip() for name in bar]
            return names_list
