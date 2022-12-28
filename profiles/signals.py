from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Notification
from recipes.models import Recipe, Comment


# code to connect Profile database to User from tutorial at
# https://www.youtube.com/watch?v=Kc1Q_ayAeQk
@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    """
    Signal creates new profile after user registers, checks if creating or
    updating profile first
    """
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()


@receiver(post_save, sender=Recipe)
def notify_of_recipe_removal(sender, instance, created, **kwargs):
    """
    Signal to create notification of recipe removal when admin removes recipe
    """
    if instance.removed:
        Notification.objects.create(
            to=instance.author.profile,
            sender=User.objects.filter(username='recipebook')[0],
            message=f'Your recipe for {instance.title} has been removed'
            )


@receiver(post_save, sender=Comment)
def notify_of_comment_removal(sender, instance, created, **kwargs):
    """
    Signal to create notification of comment removal when admin removes comment
    """
    if instance.removed:
        Notification.objects.create(
            to=instance.commenter.profile,
            sender=User.objects.filter(username='recipebook')[0],
            message=f'Your comment on {instance.recipe.title} has been removed'
            )
