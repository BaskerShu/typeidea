# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-18 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180118_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pv',
            field=models.TextField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='uv',
            field=models.IntegerField(default=0),
        ),
    ]
