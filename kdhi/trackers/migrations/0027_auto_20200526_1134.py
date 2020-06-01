# Generated by Django 2.2.5 on 2020-05-26 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0026_auto_20200515_0907'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country_list',
            options={'ordering': ('country',)},
        ),
        migrations.AlterModelOptions(
            name='overseas_topic',
            options={'ordering': ('topic',)},
        ),
        migrations.AlterField(
            model_name='inter_korean_tracker',
            name='meeting_topics',
            field=models.ManyToManyField(blank=True, to='trackers.overseas_topic'),
        ),
        migrations.AlterField(
            model_name='overseas_tracker',
            name='country_choices',
            field=models.ManyToManyField(blank=True, to='trackers.country_list'),
        ),
        migrations.AlterField(
            model_name='overseas_tracker',
            name='overseas_topics',
            field=models.ManyToManyField(blank=True, to='trackers.overseas_topic'),
        ),
        migrations.AlterField(
            model_name='overseas_tracker',
            name='participant_DPRK',
            field=models.ManyToManyField(blank=True, to='main_site.individual'),
        ),
    ]