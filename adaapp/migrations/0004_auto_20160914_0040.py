# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adaapp', '0003_auto_20160901_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='trivia_points',
            field=models.IntegerField(default=0, verbose_name='Puntos Trivia'),
        ),
        migrations.AddField(
            model_name='agent',
            name='verified_level',
            field=models.IntegerField(default=0, verbose_name='Nivel de verificación'),
        ),
    ]
