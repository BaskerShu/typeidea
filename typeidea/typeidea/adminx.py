# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xadmin
from xadmin.views import CommAdminView


class BaseOwnerAdmin(object):
    '''
    1. 用来处理文章、分类、标签、侧边栏、友链这些model的owner字段自动补充
    2. 用来针对queryset过滤当前用户的数据
    '''
    def get_list_queryset(self):
        request = self.request
        qs = super(BaseOwnerAdmin, self).get_list_queryset()
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=request.user)

    def save_models(self):
        if not self.org_obj:
            self.new_obj.owner = self.request.user
        super(BaseOwnerAdmin, self).save_models()


class GlobalSetting(object):
    site_title = "Typeidea后台管理系统"
    site_footer = "POWER BY ysz.com"


xadmin.site.register(CommAdminView, GlobalSetting)
