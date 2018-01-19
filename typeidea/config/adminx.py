# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xadmin
from xadmin.layout import Fieldset
from django.urls import reverse
from django.utils.html import format_html

from .models import Link
from .models import SideBar
from .adminforms import SideBarAdminForm
from typeidea.adminx import BaseOwnerAdmin


class LinkAdmin(BaseOwnerAdmin):
    list_display = ['title', 'href_show', 'status', 'weight', 'owner', 'created_time']
    list_display_links = None
    list_filter = ['status', 'owner']
    search_fields = ['title', 'href', 'owner__username']
    date_hierarchy = 'created_time'

    # 编辑界面
    exclude = ['owner', ]

    form_layout = (
        Fieldset(
            "信息填写",
            'title',
            'href',
            'weight',
        ),
        Fieldset(
            '状态修改',
            'status',
        )
    )

    def href_show(self, obj):
        return format_html(
            '<a href={}>{}</a>',
            *(obj.href, obj.href)
        )
    href_show.short_description = '链接'


class SideBarAdmin(BaseOwnerAdmin):
    form = SideBarAdminForm

    list_display = ['title', 'display_type', 'content', 'owner', 'created_time']
    list_display_links = None
    list_filter = ['display_type', 'owner']
    date_hierarchy = 'created_time'

    # 编辑界面
    fields = ('title', 'display_type', 'content')

    def operator(self, obj):
        return format_html(
            '<a href={}>编辑</a>',
            reverse('cus_admin:config_sidebar_change', args=(obj.id, ))
        )
    operator.short_description = '操作'


xadmin.site.register(Link, LinkAdmin)
xadmin.site.register(SideBar, SideBarAdmin)
