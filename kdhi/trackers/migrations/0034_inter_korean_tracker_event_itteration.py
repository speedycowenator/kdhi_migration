# Generated by Django 2.2.5 on 2020-06-26 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0033_auto_20200626_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='inter_korean_tracker',
            name='event_itteration',
            field=models.CharField(default='1', max_length=2),
        ),
    ]
