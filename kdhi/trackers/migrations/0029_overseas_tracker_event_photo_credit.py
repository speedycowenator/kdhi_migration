# Generated by Django 2.2.5 on 2020-06-13 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0028_auto_20200601_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='overseas_tracker',
            name='event_photo_credit',
            field=models.CharField(default='MOU', max_length=100),
        ),
    ]