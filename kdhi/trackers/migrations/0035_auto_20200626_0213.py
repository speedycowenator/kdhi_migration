# Generated by Django 2.2.5 on 2020-06-26 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0034_inter_korean_tracker_event_itteration'),
    ]

    operations = [
        migrations.AddField(
            model_name='inter_korean_tracker',
            name='media_coverage',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='inter_korean_tracker',
            name='document_link',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='inter_korean_tracker',
            name='event_photo',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='inter_korean_tracker',
            name='event_photo_add_1',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='inter_korean_tracker',
            name='event_photo_add_2',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='inter_korean_tracker',
            name='event_photo_add_3',
            field=models.URLField(blank=True, max_length=500),
        ),
    ]