import os
from datetime import timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-d#056#5ibs#5o$l49g3vho%ywse(#z(0s*n$9)pjzin9t0gpjs'
)

DEBUG = os.environ.get('DJANGO_DEBUG_VALUE') == 'True' or True

ALLOWED_HOSTS = ['*']
