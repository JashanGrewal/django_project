# Generated by Django 2.1.7 on 2019-04-21 06:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contact',
            field=models.CharField(max_length=10, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'only numbers allowed')]),
        ),
    ]
