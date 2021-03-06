# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-13 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediacenter', '0007_auto_20160318_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='lang',
            field=models.CharField(blank=True, choices=[('am', 'አማርኛ'), ('ar', 'العربية'), ('bm', 'Bambara'), ('de', 'Deutsch'), ('el', 'Ελληνικά'), ('en', 'English'), ('fa', 'فارسی'), ('fr', 'Français'), ('it', 'Italiano'), ('ku', 'Kurdî'), ('ln', 'Lingála'), ('ps', 'پښتو'), ('rn', 'Kirundi'), ('so', 'Af-Soomaali'), ('sw', 'Swahili'), ('ti', 'ትግርኛ'), ('ur', 'اردو'), ('vi', 'Tiếng Việt'), ('es', 'Español')], max_length=10, verbose_name='Language'),
        ),
    ]
