from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify
from utils.constants import TAGS
# https://stackoverflow.com/questions/837828/how-do-i-create-a-slug-in-django


class Recipe(models.Model):

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    caption = models.TextField(blank=True, null=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipe_posts'
        )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    ingredients = models.TextField()
    steps = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(
        User,
        related_name='recipe_likes',
        blank=True
        )
    tags = models.CharField(max_length=200, blank=True)
    removed = models.BooleanField(default=False)
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # https://stackoverflow.com/questions/33176569/slugfield-in-django-and-overriding-save
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)

    # code from CI 'I Think Therefore I Blog' WT project
    def count_likes(self):
        return self.likes.count()

    def count_comments(self):
        return self.recipe_comments.filter(removed=False).count()

    def list_of_tags(self):
        return eval(self.tags)
    
    def count_saved_by(self):
        return self.saved_by.count()
        

class Comment(models.Model):
    """"""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    removed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.commenter}: {self.body}"
