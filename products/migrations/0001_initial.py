# Generated by Django 3.0.7 on 2020-06-05 19:16

import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(upload_to='images')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('admin_tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=40), size=7)),
                ('user_tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=40), default=list, size=7)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]