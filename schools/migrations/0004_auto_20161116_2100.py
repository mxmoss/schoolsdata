# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 05:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0003_auto_20161116_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='School',
            field=models.CharField(max_length=255),
        ),
    ]
