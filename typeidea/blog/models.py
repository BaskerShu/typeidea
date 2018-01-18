# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import markdown

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    STATUS_ITEMS = (
        (1, '上线'),
        (2, '草稿'),
        (3, '删除'),
    )

    title = models.CharField(max_length=50, verbose_name="标题")
    desc = models.CharField(max_length=255, blank=True, verbose_name="摘要")
    category = models.ForeignKey('Category', verbose_name="分类")
    tag = models.ManyToManyField('Tag', verbose_name="标签")

    is_markdown = models.BooleanField(default=True, verbose_name="使用markdown格式")
    content = models.TextField(verbose_name='内容', help_text="注：目前仅支持markdown格式")
    html = models.TextField(verbose_name='html内容', null=True, help_text="markdown格式的内容经过转换成为html内容")
    status = models.IntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    owner = models.ForeignKey(User, verbose_name="作者")

    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def status_show(self):
        return '当前状态: {!s}'.format(self.status)
    status_show.short_description = '状态显示'

    def save(self, *args, **kwargs):
        if self.is_markdown:
            config = {
                'codehilite': {
                    'use_pygments': False,
                    'css_class': 'prettyprint linenums code-padding',
                }
            }
            self.html = markdown.markdown(
                self.content,
                extensions=["codehilite"],
                extension_configs=config
            )
        else:
            self.html = ""
        return super(Post, self).save()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = "文章"
        ordering = ['-id', ]


class Category(models.Model):
    STATUS_ITEMS = (
        (1, '可用'),
        (2, '删除'),
    )

    name = models.CharField(max_length=50, verbose_name="名称")
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    is_nav = models.BooleanField(default=False, verbose_name="是否为导航")

    owner = models.ForeignKey(User, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def nav_show(self):
        return '是' if self.is_nav else '否'
    nav_show.short_description = '是否为导航'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "分类"


class Tag(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
    )

    name = models.CharField(max_length=10, verbose_name="名称")
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")

    owner = models.ForeignKey(User, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "标题"
