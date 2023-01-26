# Generated by Django 4.0.1 on 2022-01-07 03:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('arisan', '0023_room_count'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='payment',
            unique_together={('user', 'room', 'started_at')},
        ),
    ]
