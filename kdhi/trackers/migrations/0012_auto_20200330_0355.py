# Generated by Django 2.2.5 on 2020-03-30 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0011_auto_20200330_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inter_korean_tracker',
            name='DPRK_head',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dprk_head', to='main_site.individual'),
        ),
        migrations.AlterField(
            model_name='inter_korean_tracker',
            name='ROK_head',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rok_head', to='main_site.rok_individual'),
        ),
        migrations.AlterField(
            model_name='inter_korean_tracker',
            name='participant_DPRK',
            field=models.ManyToManyField(blank=True, null=True, related_name='dprk_delegation', to='main_site.individual'),
        ),
        migrations.AlterField(
            model_name='inter_korean_tracker',
            name='participant_ROK',
            field=models.ManyToManyField(blank=True, null=True, related_name='rok_delegation', to='main_site.rok_individual'),
        ),
    ]