# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-01 15:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='models',
            new_name='phoneno',
        ),
    ]