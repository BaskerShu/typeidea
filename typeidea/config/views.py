# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.list import ListView

from .models import Link
from blog.views import CommonContextMixin


class LinkView(CommonContextMixin, ListView):
    model = Link
    template_name = 'config/link.html'
    context_object_name = 'links'

    def get_context_data(self, **kwargs):
        valid_links = []
        invalid_links = []
        links = Link.objects.all()
        for link in links:
            if link.status == 1:
                valid_links.append(link)
            elif link.status == 2:
                invalid_links.append(link)

        return super(LinkView, self).get_context_data(
            invalid_links=invalid_links,
            valid_links=valid_links
        )
