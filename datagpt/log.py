import sys

from loguru import logger as _logger

from datagpt.util import root


def get_logger(print_level="INFO", logfile_level="DEBUG"):
    _logger.remove()
    _logger.add(sys.stderr, level=print_level)

    _logger.add(root / "logs/log.txt", level=logfile_level)
    return _logger


logger = get_logger()
