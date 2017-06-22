# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-21 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0010_auto_20170620_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='DanceStyleCountType',
            fields=[
                ('abstracttype_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entities.AbstractType')),
                ('title', models.CharField(blank=True, choices=[('SOLO', 'Одиночный'), ('PARTNER', 'Парный'), ('GROUP', 'Групповой')], max_length=10)),
            ],
            bases=('entities.abstracttype',),
        ),
        migrations.CreateModel(
            name='DanceStyleDistanceType',
            fields=[
                ('abstracttype_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entities.AbstractType')),
                ('title', models.CharField(blank=True, choices=[('CLOSE', 'Близкая'), ('AVERAGE', 'Средняя'), ('DISTANT', 'Далекая')], max_length=10)),
            ],
            bases=('entities.abstracttype',),
        ),
        migrations.AddField(
            model_name='dancestyle',
            name='count_types',
            field=models.ManyToManyField(blank=True, to='entities.DanceStyleCountType'),
        ),
        migrations.AddField(
            model_name='dancestyle',
            name='distance_types',
            field=models.ManyToManyField(blank=True, to='entities.DanceStyleDistanceType'),
        ),
    ]
