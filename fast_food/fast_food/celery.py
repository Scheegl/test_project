import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fast_food.settings')

app = Celery('fast_food')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'print_every_5_seconds': {
        'task': 'board.tasks.printer',
        'schedule': 5,
        'args': (5,),
    },
}