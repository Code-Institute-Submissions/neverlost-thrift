# Generated by Django 3.0.7 on 2020-07-01 07:39

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_auto_20200701_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]