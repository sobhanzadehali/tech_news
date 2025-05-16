import os
import django
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techNews.settings')

app = Celery('techNews')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()