import sys

from loguru import logger

from eddrit import config

__version__ = "0.6.2"

logger.remove()
logger.add(sys.stderr, level=config.LOG_LEVEL)
