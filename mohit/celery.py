import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mohit.settings')

app = Celery('mohit')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
