# Generated by Django 2.2.5 on 2020-05-03 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0020_remove_collection_timeline_item_collection'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection_timeline_item',
            options={'ordering': ('year', 'month_int')},
        ),
        migrations.AddField(
            model_name='collection_timeline_item',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='documents.document_collection'),
        ),
    ]
