from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# code to connect Profile database to User from tutorial at
# https://www.youtube.com/watch?v=Kc1Q_ayAeQk
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):

    if not created:
        instance.profile.save()
