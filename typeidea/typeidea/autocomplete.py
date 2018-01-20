# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from dal import autocomplete

from blog.models import Tag, Category


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # 防止未登录的用户窃取信息
        if not self.request.user.is_authenticated():
            return Category.objects.none()

        qs = Category.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # 防止未登录的用户窃取信息
        if not self.request.user.is_authenticated():
            return Tag.objects.none()

        qs = Tag.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs
