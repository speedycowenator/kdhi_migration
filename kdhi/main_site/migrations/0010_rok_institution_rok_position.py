# Generated by Django 2.2.5 on 2020-03-13 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0009_auto_20200313_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='rok_institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('name_korean', models.CharField(max_length=200)),
                ('tag_one', models.CharField(blank=True, max_length=200)),
                ('tag_two', models.CharField(blank=True, max_length=200)),
                ('tag_three', models.CharField(blank=True, max_length=200)),
                ('function', models.TextField(max_length=20000)),
                ('additional_information', models.TextField(blank=True, max_length=20000)),
            ],
        ),
        migrations.CreateModel(
            name='rok_position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('appointment_date', models.DateField(blank=True, null=True)),
                ('confirmation_date', models.DateField(blank=True, null=True)),
                ('confirmation_src', models.CharField(default='N/A', max_length=200)),
                ('replaced', models.CharField(blank=True, max_length=200)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_site.rok_institution')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_site.rok_individual')),
            ],
        ),
    ]
