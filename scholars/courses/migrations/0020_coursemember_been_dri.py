# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_auto_20170813_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemember',
            name='been_dri',
            field=models.BooleanField(default=False),
        ),
    ]
