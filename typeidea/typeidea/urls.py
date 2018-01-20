# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xadmin

from django.conf.urls import url, include

from .autocomplete import CategoryAutocomplete, TagAutocomplete


xadmin.autodiscover()

urlpatterns = [
    url(r'^blog/', include('blog.urls')),
    url(r'^link/', include('config.urls')),
    url(r'^comment/', include('comment.urls')),
    url(r'^admin/', xadmin.site.urls),
    url(
        r'^category-autocomplete/$',
        CategoryAutocomplete.as_view(),
        name='category-autocomplete',
    ),
    url(
        r'^tag-autocomplete/$',
        TagAutocomplete.as_view(),
        name='tag-autocomplete',
    ),
]
