# Generated by Django 2.2.5 on 2020-05-01 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0046_remove_rok_institution_additional_information'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rok_institution',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='individual',
            name='full_resolution_photo',
            field=models.URLField(blank=True, default='1_Outline_Blank'),
        ),
        migrations.AlterField(
            model_name='individual',
            name='icon',
            field=models.URLField(blank=True, default='1_Outline_Blank'),
        ),
        migrations.AlterField(
            model_name='rok_individual',
            name='sources',
            field=models.TextField(default='[*] Official Ministry Website', max_length=500),
        ),
        migrations.AlterField(
            model_name='rok_institution',
            name='sources_add',
            field=models.TextField(blank=True, default='[*] Official Ministry Website', max_length=20000),
        ),
    ]
