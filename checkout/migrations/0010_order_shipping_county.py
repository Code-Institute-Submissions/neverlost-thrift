# Generated by Django 3.0.7 on 2020-07-01 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_auto_20200701_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_county',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
