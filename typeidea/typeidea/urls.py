# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xadmin
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

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
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
