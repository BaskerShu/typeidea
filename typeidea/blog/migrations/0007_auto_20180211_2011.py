# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-11 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180211_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text='\u6ce8\uff1a\u76ee\u524d\u4ec5\u4ec5\u652f\u6301markdown\u683c\u5f0f', verbose_name='\u5185\u5bb9'),
        ),
    ]
