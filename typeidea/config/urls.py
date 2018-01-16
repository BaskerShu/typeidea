# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import LinkView

urlpatterns = [
    url(r'^$', LinkView.as_view(), name='link'),
]
