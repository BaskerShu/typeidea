# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    STATUS_ITEMS = {
        (1, "正常"),
        (2, "删除"),
    }
    target = models.CharField(max_length=200, null=True, verbose_name="评论目标")
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    content = models.CharField(max_length=2000, verbose_name="内容")

    owner = models.ForeignKey(User, verbose_name="评论人")

    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name = verbose_name_plural = "评论"
