# Generated by Django 2.2.5 on 2020-06-17 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0030_auto_20200613_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='inter_korean_tracker',
            name='event_photo_credit',
            field=models.CharField(default='MOU', max_length=100),
        ),
    ]
