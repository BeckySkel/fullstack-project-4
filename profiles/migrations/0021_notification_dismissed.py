# Generated by Django 3.2.16 on 2022-12-20 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0020_auto_20221213_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='dismissed',
            field=models.BooleanField(default=False),
        ),
    ]
