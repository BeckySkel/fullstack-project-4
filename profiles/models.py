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

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_image = CloudinaryField('image', default='profile_placeholder')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def number_of_recipes(self):
        return user.objects.annotate(total_recipes=Count('recipe'))