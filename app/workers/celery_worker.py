from celery import Celery

celery = Celery(
    "ieodp",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

@celery.task
def process_resume(data):
    print("Processing resume:", data)
    return "Resume processed successfully"
