# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-13 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0003_auto_20190513_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='required',
            field=models.CharField(default='', max_length=200, verbose_name='是否必输'),
        ),
    ]
