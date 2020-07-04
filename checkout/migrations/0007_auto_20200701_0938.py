# Generated by Django 3.0.7 on 2020-07-01 07:38

import checkout.models
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_auto_20200701_0635'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='county',
            new_name='billing_county',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='full_name',
            new_name='billing_full_name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='phone_number',
            new_name='billing_phone_number',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='postcode',
            new_name='billing_postcode',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='street_address_1',
            new_name='billing_street_address_1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='street_address_2',
            new_name='billing_street_address_2',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='town_or_city',
            new_name='billing_town_or_city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='country',
        ),
        migrations.AddField(
            model_name='order',
            name='billing_country',
            field=django_countries.fields.CountryField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_country',
            field=django_countries.fields.CountryField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_full_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_phone_number',
            field=checkout.models.CustomPhoneNumberField(default='', max_length=128, region=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_postcode',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_street_address_1',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_street_address_2',
            field=models.CharField(blank=True, default='', max_length=80),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_town_or_city',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]