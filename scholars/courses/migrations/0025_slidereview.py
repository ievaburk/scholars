# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-31 13:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0024_auto_20170824_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlideReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('feedback', models.TextField(blank=True, max_length=5000, null=True)),
                ('status', models.PositiveIntegerField(choices=[(1, b'Proposed'), (2, b'Resolved')], default=1)),
                ('stage', models.PositiveIntegerField(choices=[(1, b'Peer Review'), (2, b'Refine')], default=1)),
                ('slide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='courses.Slide')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
