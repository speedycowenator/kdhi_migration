# Generated by Django 2.2.5 on 2020-06-24 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_archive', '0006_auto_20200624_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uritv_video',
            name='category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='uritv_video',
            name='category_translated',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='uritv_video',
            name='date',
            field=models.DateField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='uritv_video',
            name='description',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='uritv_video',
            name='description_translated',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='uritv_video',
            name='english_keyword',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='uritv_video',
            name='file_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='uritv_video',
            name='korean_keyword',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='uritv_video',
            name='korean_keyword_translated',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='uritv_video',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='uritv_video',
            name='title_translated',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='uritv_video',
            name='uri_source',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
