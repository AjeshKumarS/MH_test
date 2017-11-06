# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mhsite', '0007_auto_20171105_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='keam',
            field=models.IntegerField(default=0, verbose_name='KEAM Mark'),
        ),
        migrations.AlterField(
            model_name='application',
            name='plus_2',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='% of Mark Obtained in +2'),
        ),
    ]