from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    """"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    joined_on = models.DateField(auto_now=True)
    profile_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.user

    def full_name(self):
        return f"{self.first_name} {self.last_name}"