from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Account, Profile


@receiver(post_save, sender=Account)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
