# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render

from .models import Post, Tag


def post_list(request, category_id=None, tag_id=None):
    if category_id:
        # 根据分类显示文章列表
        queryset = Post.objects.filter(category_id=category_id)
    elif tag_id:
        # 根据标签显示文章列表
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            queryset = []
        else:
            queryset = tag.post_set.all()
    else:
        # 显示所有文章列表
        queryset = Post.objects.all()
    context = {
        'posts': queryset,
    }
    return render(request, 'blog/list.html', context)


def post_detail(request, post_id=None):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("post does not exist")
    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)
