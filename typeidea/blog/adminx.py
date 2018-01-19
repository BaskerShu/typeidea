# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xadmin

from django.urls import reverse
from django.utils.html import format_html
from xadmin.layout import Fieldset, Row

from .adminforms import PostAdminForm
from .models import Post, Tag, Category
from typeidea.adminx import BaseOwnerAdmin


class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm

    list_display = ['title', 'category', 'content', 'status',
                    'pv', 'uv', 'owner', 'created_time']
    list_display_links = None
    list_filter = ['category', 'owner']
    search_fields = ['title', 'category__name']
    show_full_result_count = False

    # 编辑界面
    exclude = ('html', 'pv', 'uv', 'owner')

    form_layout = (
        Fieldset(
            "基础信息",
            'title',
            'desc',
            Row('category', 'status', 'is_markdown'),
            'content',
            'tag',
        ),
    )

    def operator(self, obj):
        return format_html(
            '<a href={}>编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'


class TagAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'owner', 'created_time']
    list_display_links = None
    list_filter = ['owner']
    search_fields = ['name', 'owner__username']

    # 编辑界面
    exclude = ('owner', 'operatior')
    fields = (
        'name', 'status',
    )

    def operator(self, obj):
        return format_html(
            '<a href={}>编辑</a>',
            reverse('cus_admin:blog_tag_change', args=(obj.id,))
        )
    operator.short_description = '操作'


class CategoryAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'nav_show', 'owner', 'created_time']
    list_display_links = None
    list_filter = ['owner', 'status']
    search_fields = ['name', 'status', 'owner_username']

    # 编辑界面
    fields = ('name', 'status', 'is_nav', )

    def operator(self, obj):
        return format_html(
            '<a href={}>编辑</a>',
            reverse('cus_admin:blog_category_change', args=(obj.id,))
        )
    operator.short_description = '操作'


xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Category, CategoryAdmin)
