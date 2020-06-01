# Generated by Django 2.2.5 on 2020-05-27 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0055_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='glossary_item',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='position',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='rok_individual',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='rok_institution',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='rok_position',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
    ]