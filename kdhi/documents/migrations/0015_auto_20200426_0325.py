# Generated by Django 2.2.5 on 2020-04-26 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0014_auto_20200423_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection_timeline_item',
            name='year',
            field=models.FloatField(),
        ),
    ]
