# Generated by Django 2.2.5 on 2020-03-09 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='individual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('name_korean', models.CharField(max_length=200)),
                ('icon', models.URLField()),
                ('full_resolution_photo', models.URLField()),
                ('photo_credit', models.CharField(max_length=200)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('hometown', models.CharField(max_length=200)),
                ('education', models.CharField(max_length=200)),
                ('bio', models.CharField(max_length=2000)),
                ('sources', models.CharField(max_length=500)),
                ('video_source', models.URLField()),
                ('video_caption', models.CharField(max_length=200)),
                ('video_2_source', models.URLField()),
                ('video_2_caption', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('name_korean', models.CharField(max_length=200)),
                ('tag_one', models.CharField(max_length=200)),
                ('tag_two', models.CharField(max_length=200)),
                ('tag_three', models.CharField(max_length=200)),
                ('function', models.CharField(max_length=2000)),
                ('additional_information', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('appointment_date', models.CharField(max_length=200)),
                ('confirmation_date', models.CharField(max_length=200)),
                ('confirmation_src', models.CharField(max_length=200)),
                ('replaced', models.CharField(max_length=200)),
            ],
        ),
    ]
