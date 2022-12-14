# Generated by Django 3.2.16 on 2022-11-27 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0003_remove_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='joined_on',
        ),
        migrations.AddField(
            model_name='profile',
            name='removed_recipes',
            field=models.ManyToManyField(blank=True, related_name='removed_recipes', to='recipes.Recipe'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
