from celery import shared_task
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_verification_email(user_email):
    try:
        subject = 'Welcome'
        message = f'Welcome to the test blog application'
        from_email = 'foliocoins@gmail.com'
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        logger.info(f"Verification email sent to {user_email}")
    except Exception as e:
        # Log the exception
        logger.error(f"Failed to send verification email to {user_email}: {e}")
