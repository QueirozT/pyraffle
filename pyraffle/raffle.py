from random import choice, sample
from loguru import logger
from pyraffle.log_handlers import Handler


class Raffle:
    def __init__(self, names_list):
        self._handler = Handler()
        self._names_list = names_list
        self._shuffled_names_list = self.shuffle_list()

    @property
    def names_list(self):
        return self._names_list

    @property
    def shuffled_names_list(self):
        return self._shuffled_names_list

    def shuffle_list(self):
        shuffled_names_list = sample(self.names_list, len(self.names_list))
        return shuffled_names_list

    def draft(self, valid_number_of_winners, number_of_winners, unique):
        if valid_number_of_winners:
            while number_of_winners > 0:
                winner = choice(self.shuffled_names_list)
                if unique:
                    self.shuffled_names_list.remove(winner)
                logger.info(winner)
                number_of_winners -= 1
        else:
            logger.error(
                'Insira uma quantidade a ser sorteada que seja menor que a quantidade de nomes carregados'
            )