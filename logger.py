import logging 
from logging.config import dictConfig

def get_logger(logger: str, log_level: str = 'INFO') -> logging.Logger:
    config={
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '[%(filename)s:%(lineno)s - %(funcName)20s()] %(asctime)s %(message)s'

            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'stream': 'ext://sys.stdout',
                'level': log_level
            },
            'file':{
                'level': log_level,
                'class': 'logging.handlers.RotatingFileHandler',
                'maxBytes': 500000,
                'backupCount': 10,
                'filename': 'log_file.log',
                'formatter': 'default',
            }
        },
        'loggers': {
            '': {
                'handlers': ['file', 'console'],
                'level': log_level,
                'propagate': False
            },
        }

    }

    dictConfig(config)
    return logging.getLogger(logger)