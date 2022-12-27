from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from recipes.models import Recipe
from django.db.models import Count    


class Profile(models.Model):
    """
    Model to store extra information about the user.
    Created/updated/deleted automatically when a new user is
    added/updated/deleted 
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
        )
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    # profile_image = CloudinaryField('image', default='profile_placeholder')
    profile_image = models.ImageField(upload_to='images/', blank=True)
    bio = models.TextField(blank=True)
    saved = models.ManyToManyField(
        Recipe,
        related_name='saved_by',
        blank=True
        )

    def __str__(self):
        return self.user.username

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def count_notifications(self):
        return self.notifications.filter(dismissed=False).count()

    def count_saved_recipes(self):
        return self.saved.count()


class Notification(models.Model):
    """
    Model for user notifications
    """
    
    to = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='notifications')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    sent = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    dismissed = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification of {self.message} from {self.sender}'


class Note(models.Model):
    """"""

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='notes_for_recipe', blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='notes_from_profile')
    body = models.TextField()

    def __str__(self):
        return f'{self.profile} about {self.recipe}'