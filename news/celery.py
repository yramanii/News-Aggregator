from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from .settings import BROKER_URL, BACKEND_URL

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news.settings')

app = Celery('news', broker=BROKER_URL, backend=BACKEND_URL)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()