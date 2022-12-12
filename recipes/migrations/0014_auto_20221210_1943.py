# Generated by Django 3.2.16 on 2022-12-10 19:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0013_alter_recipe_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='saved',
            field=models.ManyToManyField(blank=True, related_name='savers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
