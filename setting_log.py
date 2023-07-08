import logging 
from logging.config import dictConfig

LOG_LEVEL = 'info'


def get_logger(logger_name : str, log_level: str = 'INFO') -> logging.Logger:
    logger_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '[%(filename)s:%(lineno)s - %(funcName)20s()]'
            }
        }
    }
