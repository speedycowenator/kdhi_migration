# Generated by Django 2.2.5 on 2020-03-23 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0018_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='bluff',
            field=models.TextField(default='FIX BLUF', max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='icon_image',
            field=models.CharField(default='NULL', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.CharField(default='FIX SLUG', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='FIX TITLE', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='individual',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
    ]
