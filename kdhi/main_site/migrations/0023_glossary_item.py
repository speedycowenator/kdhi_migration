# Generated by Django 3.0.4 on 2020-03-24 17:30

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0022_article_update_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='glossary_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('image_src', models.CharField(max_length=200)),
                ('bluff_content', models.CharField(max_length=500)),
                ('content', djrichtextfield.models.RichTextField()),
            ],
        ),
    ]