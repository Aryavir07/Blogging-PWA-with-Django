# Generated by Django 3.1.3 on 2020-12-13 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='likes',
        ),
    ]
