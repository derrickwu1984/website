# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-08 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190508_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='list_flag',
            field=models.CharField(default='', max_length=30, verbose_name='list_flag'),
        ),
    ]
