# Generated by Django 2.1.7 on 2019-02-25 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190225_0612'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor',
            name='gender',
            field=models.CharField(default='gender', max_length=20),
        ),
    ]
