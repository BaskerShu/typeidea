# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import CommentView

urlpatterns = [
    url(r'^$', CommentView.as_view(), name='comment'),
]
