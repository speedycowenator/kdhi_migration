# Generated by Django 2.2.5 on 2020-05-15 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0019_overseas_tracker_event_coverage'),
    ]

    operations = [
        migrations.AddField(
            model_name='overseas_tracker',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]