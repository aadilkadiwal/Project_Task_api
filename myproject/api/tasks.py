from celery import shared_task
from celery.contrib import rdb
import time

@shared_task
def send_email(email_id, message):
    time.sleep(10)
    rdb.set_trace()
    print("Email is sent to {email_id}. Message sent was - {message}")    