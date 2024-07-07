from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Contractor


def send_email(subject, message, recipient_list):
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=recipient_list,
        fail_silently=False,
    )


@receiver(post_save, sender=Contractor)
def send_arrival_email(sender, instance, created, **kwargs):
    worker_email = instance.responsible_worker.email
    if created and instance.arriving_time:
        subject = 'Arrival Notification'
        message = f'{instance.company} has arrived at {instance.arriving_time}.'
        send_email(subject=subject, message=message, recipient_list=[worker_email])
    elif not created and 'arriving_time' in instance.get_dirty_fields():
        subject = 'Update Arrival Notification'
        message = f'{instance.company} has arrived at {instance.arriving_time}.'
        send_email(subject=subject, message=message, recipient_list=[worker_email])


@receiver(post_save, sender=Contractor)
def send_leaving_email(sender, instance, **kwargs):
    worker_email = instance.responsible_worker.email
    if instance.leaving_time and 'leaving_time' in instance.get_dirty_fields():
        subject = 'Leaving Notification'
        message = f'{instance.company} has left at {instance.leaving_time}.'
        send_email(subject=subject, message=message, recipient_list=[worker_email])
