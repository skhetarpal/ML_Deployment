import logging
import sys

LOGGER_NAME = 'house_price_predictor'


def basic_logger(*, name: str) -> logging.Logger:
    
    formatter = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s —" "%(funcName)s:%(lineno)d — %(message)s")
    handler = logging.StreamHandler(stream=sys.stdout).setLevel(logging.DEBUG).setFormatter(formatter)
    logger = logging.getLogger(name).setLevel(logging.DEBUG).addHandler(handler)
    logger.propagate = False
    
    return logger
    