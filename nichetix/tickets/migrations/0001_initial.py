# Generated by Django 3.2.6 on 2021-09-16 13:39

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0004_location_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ticket name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique_with=('event',), verbose_name='Ticket type URL')),
                ('description_long', models.TextField(verbose_name='Text Description')),
                ('sale_start', models.DateTimeField(verbose_name='Sale Start')),
                ('sale_end', models.DateTimeField(verbose_name='Sale End')),
                ('quota', models.PositiveSmallIntegerField(verbose_name='Quota')),
                ('price_net', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price')),
                ('tax', models.CharField(choices=[('base', 19.0), ('cut', 7.0), ('zero', 0.0)], max_length=4, verbose_name='Tax rate')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='events.event')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Ticket id')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='id', verbose_name='Ticket URL')),
                ('bought', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tickets.tickettype')),
            ],
        ),
    ]
