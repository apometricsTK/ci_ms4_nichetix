# Generated by Django 3.2.6 on 2021-09-28 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_location_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='location',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]
