# Generated by Django 2.2.5 on 2020-06-26 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0032_auto_20200626_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inter_korean_tracker',
            name='document_name',
            field=models.CharField(default='No Document Available', max_length=1000),
        ),
    ]
