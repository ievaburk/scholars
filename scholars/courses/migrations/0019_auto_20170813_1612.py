# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 16:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_auto_20170813_1124'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='course',
            unique_together=set([('name', 'lang', 'version')]),
        ),
    ]