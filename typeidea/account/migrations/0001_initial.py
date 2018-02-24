# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-22 16:20
from __future__ import unicode_literals

import account.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import typeidea.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(storage=typeidea.storage.OverwriteStorage(), upload_to=account.models.user_avatar_path, verbose_name='\u5934\u50cf')),
                ('location', models.CharField(blank=True, max_length=30, verbose_name='\u4f4d\u7f6e')),
                ('blog_site', models.URLField(blank=True, max_length=30, verbose_name='\u535a\u5ba2\u5730\u5740')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
        ),
    ]
