# -*- coding: utf-8 -*-


import os
import sys

import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'user_server.settings.unittest'
django.setup()

from django.test.runner import DiscoverRunner


"""
Run tests script
"""

test_runner = DiscoverRunner(pattern='tests.py', verbosity=2,
                             interactive=True, failfast=False)

failures = test_runner.run_tests(['user_server'])
sys.exit(failures)
