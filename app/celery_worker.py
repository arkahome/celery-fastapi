# ### celery.py
# import os
# from celery import Celery
# # set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meupBackend.settings')
# app = Celery('meupBackend', backend='redis', broker='redis://localhost:6380')
# # Using a string here means the worker doesn't have to serialize
# # the configuration object to child processes.
# # - namespace='CELERY' means all celery-related configuration keys
# #   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')
# # Load task modules from all registered Django app configs.
# app.autodiscover_tasks()
# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))

from time import sleep
from celery import Celery
from celery.utils.log import get_task_logger
# Initialize celery
celery = Celery('tasks', result_backend='redis://localhost:6380', broker_url='redis://localhost:6380',)
# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)
# Create Order - Run Asynchronously with celery
# Example process of long running task
@celery.task(name='create_order')
def create_order(name, quantity):
    
    # 5 seconds per 1 order
    complete_time_per_item = 5
    
    # Keep increasing depending on item quantity being ordered
    sleep(complete_time_per_item * quantity)
# Display log    
    celery_log.info(f"Order Complete!")
    return {"message": f"Hi {name}, Your order has completed!",
            "order_quantity": quantity}


# celery -A app.celery_worker.celery worker --loglevel=info
# pip install gevent # Windows
# celery -A app.celery_worker.celery worker --loglevel=info --pool=gevent

#Flower 
# celery --broker=redis://localhost:6380/0 flower
# uvicorn main:app --reload
# docker compose up