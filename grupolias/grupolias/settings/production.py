from .base import *

DEBUG = False

ALLOWED_HOSTS = ['164.92.112.192', 'grupolias.com', 'localhost', 'www.grupolias.com'] 

SECRET_KEY = 'z-he-j@ji!8)@qfif0-(0c8@!qr$bz_nxjixrc3an370k-xy#a'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}

try:
    from .local import *
except ImportError:
    pass
