# Generated by Django 2.2.5 on 2020-06-18 00:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_archive', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state_media_article',
            name='date_publication',
        ),
        migrations.AddField(
            model_name='state_media_article',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
