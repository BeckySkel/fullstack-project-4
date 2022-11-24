from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    caption = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_posts')
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    ingredients = models.JSONField()
    steps = models.JSONField()
    image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(
        User, related_name='recipe_likes', blank=True
        )

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()