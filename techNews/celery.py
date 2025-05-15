import os
import django
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techNews.settings')
django.setup()

app = Celery('techNews')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
