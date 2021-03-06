# Generated by Django 2.2.5 on 2020-03-13 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0008_auto_20200311_0813'),
    ]

    operations = [
        migrations.CreateModel(
            name='rok_individual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('name_korean', models.CharField(max_length=200)),
                ('icon', models.URLField(blank=True)),
                ('full_resolution_photo', models.URLField(blank=True)),
                ('photo_credit', models.CharField(blank=True, max_length=200)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('hometown', models.CharField(blank=True, max_length=200)),
                ('education', models.CharField(blank=True, max_length=200)),
                ('bio', models.TextField(max_length=20000)),
                ('sources', models.TextField(max_length=500)),
                ('video_source', models.URLField(blank=True)),
                ('video_caption', models.CharField(blank=True, max_length=200)),
                ('video_2_source', models.URLField(blank=True)),
                ('video_2_caption', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterModelOptions(
            name='individual',
            options={'ordering': ('name',)},
        ),
    ]
