# Generated by Django 2.2.5 on 2020-06-22 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0067_auto_20200622_0108'),
    ]

    operations = [
        migrations.CreateModel(
            name='dprk_institution_tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.DeleteModel(
            name='dprk_institution_tags',
        ),
        migrations.AlterField(
            model_name='institution',
            name='function_tags',
            field=models.ManyToManyField(blank=True, null=True, to='main_site.dprk_institution_tag'),
        ),
    ]
