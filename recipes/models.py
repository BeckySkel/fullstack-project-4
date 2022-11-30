from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify
from django.contrib import messages


class Recipe(models.Model):

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    caption = models.TextField(blank=True, null=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipe_posts'
        )
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    ingredients = models.TextField(blank=True, null=True)
    steps = models.TextField(blank=True, null=True)
    image = CloudinaryField('image', default='placeholder', blank=True)
    likes = models.ManyToManyField(
        User,
        related_name='recipe_likes',
        blank=True
        )
    removed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)

    # code from CI 'I Think Therefore I Blog' WT project
    def number_of_likes(self):
        return self.likes.count()