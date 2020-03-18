# Generated by Django 2.2.5 on 2020-03-16 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0016_rok_individual_name_true'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rok_position',
            name='institution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_site.rok_institution'),
        ),
        migrations.AlterField(
            model_name='rok_position',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_site.rok_individual'),
        ),
    ]
