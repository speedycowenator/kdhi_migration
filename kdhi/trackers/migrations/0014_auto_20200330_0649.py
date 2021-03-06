# Generated by Django 2.2.5 on 2020-03-30 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0013_country_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='overseas_topics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='overseas_tracker',
            name='country_choices',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='trackers.country_list'),
        ),
        migrations.AddField(
            model_name='overseas_tracker',
            name='overseas_topics',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='trackers.overseas_topics'),
        ),
    ]
