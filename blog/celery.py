from __future__ import absolute_import
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

app = Celery('blog')#, broker='amqp')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()#(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))