import sys, logging


config = {
  'version': 1, # Logging config schema, nothing to do with us.

  'formatters': {
    'st': {'format': '%(asctime)s %(name)s %(levelname)s %(message)s'},
    'fi': {'format': '%(asctime)s %(message)s'},
    },

  'handlers': {
    'console': {
      'class': 'logging.StreamHandler',
      'level': logging.DEBUG,
      'formatter': 'st',
      'stream': sys.stdout,
      },
    'disk': {
      'class': 'logging.FileHandler',
      'level': logging.INFO,
      'formatter': 'fi',
      'filename': 'sosimple.log',
      },
    },

  'loggers': {
    'sosimple': {
      'level': logging.DEBUG,
      'handlers': ['console', 'disk'],
      },
    },
  }


if __name__ == '__main__':
  import logging.config
  logging.config.dictConfig(config)
  log = logging.getLogger('sosimple')
  log.error('cats!')
