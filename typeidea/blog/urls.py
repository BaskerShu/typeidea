# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.views.decorators.cache import cache_page

from .views import IndexView, CategoryView, TagView, PostView, AuthorView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category'),
    url(r'tag/(?P<tag_id>\d+)/$', cache_page(60)(TagView.as_view()), name='tag'),
    url(r'author/(?P<author_id>\d+)/$', AuthorView.as_view(), name='author'),
    url(r'post/(?P<post_id>\d+)/$', PostView.as_view(), name='detail'),
]
