# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mhsite', '0003_auto_20171104_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item1', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('item2', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('item3', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('item4', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('item5', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
    ]