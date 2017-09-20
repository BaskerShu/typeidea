# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Comment
from .adminforms import CommentAdminForm
from typeidea.custom_site import custom_site


@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    form = CommentAdminForm

    list_display = ['post', 'content', 'nickname', 'website', 'email', 'created_time', 'operator']
    list_display_links = None
    list_filter = ['post', ]
    search_fields = ['content', 'post__name', 'nickname']

    # 编辑界面
    fieldsets = (
        ('信息填写', {
            'fields': ('nickname', 'website', 'email')
        }),
        ('评论', {
            'fields': ('post', 'content')
        })
    )

    def operator(self, obj):
        return format_html(
            '<a href={}>编辑</a>',
            reverse('cus_admin:comment_comment_change', args=(obj.id,))
        )
    operator.short_description = '操作'
