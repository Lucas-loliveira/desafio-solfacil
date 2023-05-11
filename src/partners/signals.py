import logging
from typing import Any

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Partner

logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler: logging.Handler = logging.FileHandler("welcome_emails.log")
handler.setLevel(logging.INFO)
formatter: logging.Formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(message)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)


@receiver(post_save, sender=Partner)
def send_welcome_email(
    sender: Any, instance: Partner, created: bool, **kwargs: Any
) -> None:
    if created:
        send_email(instance.email, f"Welcome email sent to {instance.email}")


def send_email(email: str, msg: str):
    logger.info(msg)
    return True
