# Generated by Django 2.2.5 on 2020-06-01 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0061_auto_20200601_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='confirmation_date',
            field=models.DateField(blank=True, default='2020-05-13', null=True),
        ),
    ]
