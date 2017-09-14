# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_title = "typeidea后台管理系统"
    site_header = "typeidea"
    index_title = "首页"


custom_site = CustomSite(name='cus_site')
