# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import IndexView, CategoryView, TagView, PostView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category'),
    url(r'tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag'),
    url(r'post/(?P<post_id>\d+)/$', PostView.as_view(), name='detail'),
]
