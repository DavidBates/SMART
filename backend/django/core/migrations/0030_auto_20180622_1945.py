# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-22 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_merge_20171108_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='active_l_method',
            field=models.TextField(default='least confident'),
        ),
        migrations.AddField(
            model_name='project',
            name='use_active_learning',
            field=models.BooleanField(default=True),
        ),
    ]
