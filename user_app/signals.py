from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile, ActivityLog

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        ActivityLog.objects.create(
            user=instance,
            activity_type='ACCOUNT_CREATED',
            details='User account was created'
        )

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()