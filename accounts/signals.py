from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Account


@receiver(post_save, sender=Account)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(username=instance)
        instance.accounts.save()
