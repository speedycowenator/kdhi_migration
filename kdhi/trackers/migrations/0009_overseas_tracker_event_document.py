# Generated by Django 2.2.5 on 2020-03-30 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0008_auto_20200330_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='overseas_tracker',
            name='event_document',
            field=models.URLField(blank=True),
        ),
    ]
