# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 05:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adaapp', '0004_auto_20160914_0040'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agent',
            options={'verbose_name': 'Agent', 'verbose_name_plural': 'Agents'},
        ),
        migrations.AlterModelOptions(
            name='faction',
            options={'verbose_name': 'Faction', 'verbose_name_plural': 'Factions'},
        ),
    ]
