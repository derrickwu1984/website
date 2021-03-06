# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-21 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.CharField(default='', max_length=200, primary_key=True, serialize=False)),
                ('trs_code', models.CharField(default='', max_length=20, verbose_name='交易码')),
                ('trs_name', models.CharField(default='', max_length=200, verbose_name='交易名称')),
                ('fuc_desc', models.CharField(default='', max_length=1000, verbose_name='交易描述')),
                ('flag', models.CharField(default='', max_length=30, verbose_name='输入输出标识')),
                ('eng_name', models.CharField(default='', max_length=200, verbose_name='英文名')),
                ('chinese_name', models.CharField(default='', max_length=200, verbose_name='中文名')),
                ('data_type', models.CharField(default='', max_length=20, verbose_name='数据类型')),
                ('required', models.CharField(default='', max_length=200, verbose_name='是否必输')),
                ('remark', models.CharField(default='', max_length=2000, verbose_name='备注')),
            ],
            options={
                'verbose_name': '接口详情',
                'verbose_name_plural': '接口详情',
            },
        ),
    ]
