# Generated by Django 2.2.5 on 2020-03-30 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0007_auto_20200315_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='inter_korean_tracker',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='overseas_tracker',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
    ]
