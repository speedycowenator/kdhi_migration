# Generated by Django 2.2.5 on 2020-06-22 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0069_dprk_institution_tag_weight'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dprk_institution_tag',
            options={'ordering': ('-weight', 'name')},
        ),
        migrations.AlterField(
            model_name='dprk_institution_tag',
            name='name',
            field=models.CharField(max_length=21),
        ),
    ]
