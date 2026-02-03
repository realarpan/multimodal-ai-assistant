from celery import Celery
from .config import get_settings

settings = get_settings()

celery = Celery(
    "multimodal",
    broker=settings.redis_url,
    backend=settings.redis_url,
)

celery.conf.task_routes = {
    "app.services.ml_inference.process_multimodal_task": {"queue": "multimodal"},
}
