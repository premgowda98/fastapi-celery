from celery import Celery 
import time

celery_app = Celery(__name__, broker="amqp://guest:guest@localhost:5672", backend="redis://localhost:6379")
celery_app.conf.update(
    broker_connection_retry_on_startup=True,
    task_track_started=True
)

@celery_app.task
def process_image():
    # simulate image_processing
    time.sleep(10)
    return True


