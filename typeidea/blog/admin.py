# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .adminforms import PostAdminForm
from .models import Post, Tag, Category
from typeidea.custom_site import custom_site


@admin.register(Post, site=custom_site)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

    list_display = ['title', 'category', 'content', 'status_show',
                    'owner', 'created_time', 'operator']
    list_display_links = []
    list_filter = ['category', 'owner']
    search_fields = ['title', 'category__name', 'owner__username']
    show_full_result_count = False

    # 编辑界面
    save_on_top = False
    fieldsets = (
        ('基础设置', {
            'fields': (
                ('title', 'category'),
                'desc',
                'status',
                'content',
            )
        }),
        ('高级配置', {
            'fields': ('tag',),
            'classes': ('collapse', 'addon'),
        })
    )
    filter_horizontal = ['tag']  # 多对多字段管理

    def operator(self, obj):
        return format_html(
            '<a href={}>编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        # import pdb;pdb.set_trace()
        obj.owner = request.user
        super(PostAdmin, self).save_model(request, obj, form, change)


class PostInline(admin.StackedInline):
    fieldsets = (
        ('基础设置', {
            'fields': (
                ('title', 'category'),
                'desc',
                'status',
                'content',
            )
        }),
        ('高级配置', {
            'fields': ('tag',),
            'classes': ('collapse', 'addon'),
        })
    )
    extra = 1
    model = Post


@admin.register(Tag, site=custom_site)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Category, site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        PostInline,
    ]
