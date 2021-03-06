# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xadmin
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic import RedirectView

from .autocomplete import CategoryAutocomplete, TagAutocomplete
from blog.api.views import PostViewSet, TagViewSet, CategoryViewSet


xadmin.autodiscover()

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='index', permanent=False)),
    url(r'^blog/', include('blog.urls')),
    url(r'^link/', include('config.urls')),
    url(r'^comment/', include('comment.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^admin/', xadmin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api/docs/', include_docs_urls(title='Typeidea api')),
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

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
