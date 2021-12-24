import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# To make a task periodic

app.conf.beat_schedule = {
    # Task name
    'every-15-seconds': {
        # Which task we have to execute
        'task': 'api.tasks.send_email',
        # Time for periodic
        'schedule': 15,
        'args': ('aadilshaan456@gmail.com','This is a Sample message.')
    }
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')