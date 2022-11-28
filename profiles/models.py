from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from recipes.models import Recipe


class Profile(models.Model):
    """"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_image = CloudinaryField('image', default='placeholder')
    removed_recipes = models.ManyToManyField(
        Recipe,
        related_name='removed_recipes',
        blank=True
        )
    

    def __str__(self):
        return self.user.username

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def number_of_removed_recipes(self):
        return self.removed_recipes.count()