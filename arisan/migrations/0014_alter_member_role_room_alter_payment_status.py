# Generated by Django 4.0 on 2021-12-30 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arisan', '0013_rename_deadline_room_intervaldate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='role_room',
            field=models.CharField(choices=[('host', 'host'), ('member', 'member')], default='member', max_length=16),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('paid', 'paid'), ('bill', 'bill')], default='bill', max_length=4),
        ),
    ]