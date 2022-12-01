from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from recipes.models import Recipe
from django.db.models import Count    


class Profile(models.Model):
    """
    Model to store extra information about the user.
    Created/deleted automatically when a new user is added/deleted 
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_image = CloudinaryField('image', default='profile_placeholder')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def number_of_notifications(self):
        return self.notifications.count()


class Notification(models.Model):
    """"""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='notifications')
    sender = models.OneToOneField(User, on_delete=models.CASCADE)
    sent = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return f'Notification of {self.message} from {self.sender}'
    
    #  def number_of_likes(self):
    #     return self.profile.count()