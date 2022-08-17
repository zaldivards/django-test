# Generated by Django 4.1 on 2022-08-16 18:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rentals',
            unique_together={('user_id', 'movie_id')},
        ),
    ]