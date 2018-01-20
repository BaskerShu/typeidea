# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xadmin
from xadmin.layout import Fieldset

from .models import Comment
from .adminforms import CommentAdminForm


class CommentAdmin(object):
    form = CommentAdminForm

    list_display = ['target', 'content', 'nickname', 'website', 'email', 'created_time', ]
    list_display_links = None
    list_filter = ['content', ]
    search_fields = ['content', 'nickname']

    # 编辑界面
    exclude = ('target', )

    form_layout = (
        Fieldset(
            "信息填写",
            'nickname',
            'website',
            'email',
            'title',
            'content',
        ),
        Fieldset(
            '状态修改',
            'status',
        )
    )


xadmin.site.register(Comment, CommentAdmin)