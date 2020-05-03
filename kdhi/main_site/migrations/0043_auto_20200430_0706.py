# Generated by Django 2.2.5 on 2020-04-30 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0042_auto_20200430_0328'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rok_position',
            options={'ordering': ('position_rank', 'person')},
        ),
        migrations.AddField(
            model_name='rok_institution',
            name='slug',
            field=models.CharField(default='blank', max_length=200),
            preserve_default=False,
        ),
    ]