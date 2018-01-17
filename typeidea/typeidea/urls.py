# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from django.contrib import admin

from .custom_site import custom_site

urlpatterns = [
    url(r'^blog/', include('blog.urls')),
    url(r'^link/', include('config.urls')),
    url(r'^comment/', include('comment.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^cus_admin/', custom_site.urls),
]
