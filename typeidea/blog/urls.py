# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='index'),
    url(r'category/(?P<category_id>\d+)/$', views.post_list, name='category'),
    url(r'tag/(?P<tag_id>\d+)/$', views.post_list, name='tag'),
    url(r'post/(?P<post_id>\d+)/$', views.post_detail, name='detail'),
]
