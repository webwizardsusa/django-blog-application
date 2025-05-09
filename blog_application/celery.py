# project_name/celery.py
import os
import json
from celery import Celery
from kombu.serialization import register

register('json', json.dumps, json.loads,content_type='application/json',content_encoding='utf-8')

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_application.settings')

app = Celery('blog_application')

# Using a string here means the worker doesn’t have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related config keys should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()