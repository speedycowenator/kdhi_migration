# Generated by Django 2.2.5 on 2020-05-12 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0026_auto_20200508_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='keywords',
            field=models.ManyToManyField(blank=True, to='documents.document_keyword'),
        ),
    ]
