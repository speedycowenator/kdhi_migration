# Generated by Django 2.2.5 on 2020-03-23 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0019_auto_20200323_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='update_date',
            field=models.DateField(),
        ),
    ]
