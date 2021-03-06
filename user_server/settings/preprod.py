# -*- coding: utf-8 -*-

from os import environ
from os.path import normpath
from .base import *


##########################
# Database configuration #
##########################

DATABASES['default']['HOST'] = '{{ default_db_host }}'
DATABASES['default']['USER'] = '{{ default_db_user }}'
DATABASES['default']['PASSWORD'] = '{{ default_db_password }}'
DATABASES['default']['NAME'] = '{{ default_db_name }}'


############################
# Allowed hosts & Security #
############################

ALLOWED_HOSTS = [
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'ssl')


##############
# Secret key #
##############

SECRET_KEY = '{{ secret_key }}'

