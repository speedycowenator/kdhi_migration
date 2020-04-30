# Generated by Django 2.2.5 on 2020-04-14 00:04

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0035_remove_institution_function_plain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='sources',
            field=djrichtextfield.models.RichTextField(blank=True, default='<a href="https://nkinfo.unikorea.go.kr/nkp/main/portalMain.do">[1]</a> Ministry of Unification, \'2019년 북한 기관별 인명록\'  2018-12-27\' Party of Korea (WPK)', null=True),
        ),
    ]