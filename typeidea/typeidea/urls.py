# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xadmin

from django.conf.urls import url, include


xadmin.autodiscover()

urlpatterns = [
    url(r'^blog/', include('blog.urls')),
    url(r'^link/', include('config.urls')),
    url(r'^comment/', include('comment.urls')),
    url(r'^admin/', xadmin.site.urls),
]
