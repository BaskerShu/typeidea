# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from blog.models import Category, Post, Tag
from config.models import SideBar
from comment.models import Comment
from comment.forms import CommentForm


class CommentShowMixin(object):
    def get_comment(self):
        target = self.request.path
        comment_list = Comment.objects.filter(target=target).order_by('-created_time')
        return comment_list

    def get_context_data(self, **kwargs):
        if 'comment_form' not in kwargs:
            kwargs.update({
                'comment_form': CommentForm(),
            })
        kwargs.update({
            'comment_list': self.get_comment(),
        })
        return super(CommentShowMixin, self).get_context_data(**kwargs)


class CommonContextMixin(object):
    def get_context_data(self, **kwargs):
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
        recently_post = Post.objects.filter(status=1)[:5]
        hot_post = Post.objects.order_by('-pv', '-id')[:8]
        recently_comment = Comment.objects.filter(status=1)[:8]

        # user
        user = self.request.user

        context = {
            'nav_cates': nav_cates,
            'cates': cates,
            'side_bars': side_bars,
            'recently_post': recently_post,
            'recently_comment': recently_comment,
            'hot_post': hot_post,
            'tags': Tag.objects.all(),
            'user': user,
        }
        context.update(kwargs)

        return super(CommonContextMixin, self).get_context_data(**context)
