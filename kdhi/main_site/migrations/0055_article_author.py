# Generated by Django 2.2.5 on 2020-05-26 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0054_article_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='KDHI', max_length=50),
        ),
    ]
