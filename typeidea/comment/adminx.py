# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xadmin
from xadmin.layout import Fieldset

from .models import Comment
from .adminforms import CommentAdminForm


class CommentAdmin(object):
    form = CommentAdminForm

    list_display = ['target', 'content', 'created_time', 'owner']
    list_display_links = None
    list_filter = ['content', ]
    search_fields = ['content', 'owner']

    # 编辑界面
    exclude = ('target', )

    form_layout = (
        Fieldset(
            "信息填写",
            'owner',
            'content',
        ),
        Fieldset(
            '状态修改',
            'status',
        )
    )


xadmin.site.register(Comment, CommentAdmin)
