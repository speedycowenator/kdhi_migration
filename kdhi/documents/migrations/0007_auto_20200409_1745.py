# Generated by Django 2.2.5 on 2020-04-09 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0006_auto_20200406_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='documents.document_collection'),
        ),
        migrations.AlterField(
            model_name='document',
            name='creator',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
