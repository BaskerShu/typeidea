# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .adminforms import PostAdminForm
from .models import Post, Tag, Category
from typeidea.custom_site import custom_site
from typeidea.custom_admin import BaseOwnerAdmin


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm

    list_display = ['title', 'category', 'content', 'status',
                    'pv', 'uv', 'owner', 'created_time', 'operator']
    list_display_links = None
    list_filter = ['category', 'owner']
    search_fields = ['title', 'category__name']
    show_full_result_count = False

    # 编辑界面
    save_on_top = False
    fields = (
        ('title', 'category'),
        'desc',
        'status',
        ('content', 'is_markdown'),
        'html',
        'tag'
    )
    filter_horizontal = ['tag']  # 多对多字段管理

    def operator(self, obj):
        return format_html(
            '<a href={}>编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'owner', 'created_time', 'operator']
    list_display_links = None
    list_filter = ['owner']
    search_fields = ['name', 'owner__username']

    # 编辑界面
    fields = (
        ('name', 'status'),
    )

    def operator(self, obj):
        return format_html(
            '<a href={}>编辑</a>',
            reverse('cus_admin:blog_tag_change', args=(obj.id,))
        )
    operator.short_description = '操作'


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'nav_show', 'owner', 'created_time', 'operator']
    list_display_links = None
    list_filter = ['owner', 'status']
    search_fields = ['name', 'status', 'owner_username']

    # 编辑界面
    fields = (('name', 'status', 'is_nav'), )

    def operator(self, obj):
        return format_html(
            '<a href={}>编辑</a>',
            reverse('cus_admin:blog_category_change', args=(obj.id,))
        )
    operator.short_description = '操作'
