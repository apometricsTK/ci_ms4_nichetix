# Generated by Django 3.2.6 on 2021-08-26 16:07

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_host',
        ),
        migrations.AddField(
            model_name='user',
            name='can_host',
            field=models.BooleanField(default=False, verbose_name='Host status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='company_name',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Name of the host company'),
        ),
        migrations.AlterField(
            model_name='user',
            name='default_country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='user',
            name='default_county',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='County'),
        ),
        migrations.AlterField(
            model_name='user',
            name='default_phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='default_postcode',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Postcode'),
        ),
        migrations.AlterField(
            model_name='user',
            name='default_street_address1',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Street address1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='default_street_address2',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Street address2'),
        ),
        migrations.AlterField(
            model_name='user',
            name='default_town_or_city',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Town or city'),
        ),
    ]
