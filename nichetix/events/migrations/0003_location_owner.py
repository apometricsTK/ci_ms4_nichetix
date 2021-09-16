# Generated by Django 3.2.6 on 2021-09-04 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_alter_event_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='users.user'),
            preserve_default=False,
        ),
    ]
