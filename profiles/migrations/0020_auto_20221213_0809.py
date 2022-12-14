# Generated by Django 3.2.16 on 2022-12-13 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0015_remove_recipe_saved'),
        ('profiles', '0019_auto_20221213_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes_from_profile', to='profiles.profile'),
        ),
        migrations.AlterField(
            model_name='note',
            name='recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes_for_recipe', to='recipes.recipe'),
        ),
    ]
