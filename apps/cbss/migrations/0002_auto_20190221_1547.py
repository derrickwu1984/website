# Generated by Django 2.1.7 on 2019-02-21 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbss', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile_userinfo_jinan',
            name='object_id',
            field=models.CharField(blank=True, default='', max_length=32, verbose_name='uuid'),
        ),
    ]