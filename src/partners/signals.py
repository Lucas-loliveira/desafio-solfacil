from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Partner
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler("welcome_emails.log")
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


@receiver(post_save, sender=Partner)
def send_welcome_email(sender, instance, created, **kwargs):
    print("ENTORUUUUU")
    print(instance)
    print(created)
    if created:
        email = instance.email
        logger.info("Welcome email sent to %s", email)
