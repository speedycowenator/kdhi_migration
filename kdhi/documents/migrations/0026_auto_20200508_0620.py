# Generated by Django 2.2.5 on 2020-05-08 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0025_document_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='keywords',
            field=models.ManyToManyField(blank=True, null=True, to='documents.document_keyword'),
        ),
    ]
