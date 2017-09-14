# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from typeidea.custom_site import custom_site
from .models import Post, Tag, Category


@admin.register(Post, site=custom_site)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'content', 'status', 'owner', 'created_time']
    list_filter = ['category', 'owner']
    search_fields = ['title', 'category__name', 'owner__username']
    show_full_result_count = False
    list_display_links = ['category', 'status']
    list_editable = ('title',)


@admin.register(Tag, site=custom_site)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Category, site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    pass
