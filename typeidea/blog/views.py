# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post, Tag, Category
from config.models import SideBar
from comment.models import Comment


def post_list(request, category_id=None, tag_id=None):
    page_size = 2
    page = request.GET.get('page', 1)

    if category_id:
        # 根据分类显示文章列表
        queryset = Post.objects.filter(category_id=category_id, status=1)
    elif tag_id:
        # 根据标签显示文章列表
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            queryset = []
        else:
            queryset = tag.post_set.filter(status=1)
    else:
        # 显示所有文章列表
        queryset = Post.objects.all()

    # 分页
    paginator = Paginator(queryset, page_size)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    # 分类导航
    nav_cates = []
    cates = []
    categories = Category.objects.filter(status=1)
    for cate in categories:
        if cate.is_nav:
            nav_cates.append(cate)
        else:
            cates.append(cate)

    # 侧边栏
    side_bars = SideBar.objects.filter(status=1)
    recently_post = Post.objects.filter(status=1)[:10]
    recently_comment = Comment.objects.filter(status=1)[:10]

    context = {
        'posts': posts,
        'nav_cates': nav_cates,
        'cates': cates,
        'side_bars': side_bars,
        'recently_post': recently_post,
        'recently_comment': recently_comment,
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
