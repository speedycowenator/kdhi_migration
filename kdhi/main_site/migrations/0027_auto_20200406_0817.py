# Generated by Django 2.2.5 on 2020-04-06 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0026_auto_20200406_0816'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ('institution', '-position_rank')},
        ),
    ]