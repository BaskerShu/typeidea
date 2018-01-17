# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-17 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_comment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='target',
            field=models.CharField(max_length=2000, null=True, verbose_name='\u8bc4\u8bba\u76ee\u6807'),
        ),
    ]
