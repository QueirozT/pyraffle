from pathlib import Path
from sys import stderr

from loguru import logger


class Handler:
    def __init__(self):
        logger.remove()
        self._logs_path = Path('logs/')
        self._logs_path.mkdir(exist_ok=True)
        logger.add(sink=self._logs_path / 'log_{time:YYYYMMDD_HHmmss}.log')
        logger.add(sink=stderr, level='INFO', format='{message}')
