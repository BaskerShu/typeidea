# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from .serializers import (PostSerializer, CategorySerializer,
                          TagSerializer, PostDetailSerializer,
                          CategoryDetailSerializer, TagDetailSerializer,)
from blog.models import Post, Category, Tag


class SwitchSerializerMixin(object):
    detail_serializer = None

    def __init__(self, *args, **kwargs):
        if not self.detail_serializer:
            self.detail_serializer = self.serializer_class

    def retrieve(self, *args, **kwargs):
        self.serializer_class = self.detail_serializer
        return super(SwitchSerializerMixin, self).retrieve(self, *args, **kwargs)


class PostViewSet(SwitchSerializerMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    detail_serializer = PostDetailSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super(PostViewSet, self).get_queryset(*args, **kwargs)
        cate_id = self.request.GET.get('cate_id')
        tag_id = self.request.GET.get('tag_id')
        if cate_id:
            qs = qs.filter(category_id=cate_id)
        if tag_id:
            qs = qs.filter(tag_id=tag_id)

        return qs


class CategoryViewSet(SwitchSerializerMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    detail_serializer = CategoryDetailSerializer


class TagViewSet(SwitchSerializerMixin, viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    detail_serializer = TagDetailSerializer
