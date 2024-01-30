from __future__ import absolute_import, unicode_literals
from django.conf import settings

import os
import logging

from celery import Celery

logger = logging.getLogger("Celery")

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

# Create a Celery instance and configure it using the settings from Django.
app = Celery('app')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all installed apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
