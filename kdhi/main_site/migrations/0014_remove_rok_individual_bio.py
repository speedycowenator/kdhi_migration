# Generated by Django 2.2.5 on 2020-03-13 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0013_auto_20200313_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rok_individual',
            name='bio',
        ),
    ]
