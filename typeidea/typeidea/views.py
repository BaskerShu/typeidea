# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from blog.models import Category, Post, Tag
from config.models import SideBar
from comment.models import Comment
from comment.forms import CommentForm


class CommentShowMixin(object):
    def get_comment(self):
        target = self.request.path
        comment_list = Comment.objects.filter(target=target)
        return comment_list

    def get_context_data(self, **kwargs):
        kwargs.update({
            'comment_form': CommentForm(),
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
        recently_post = Post.objects.filter(status=1)[:10]
        recently_comment = Comment.objects.filter(status=1)[:10]

        context = {
            'nav_cates': nav_cates,
            'cates': cates,
            'side_bars': side_bars,
            'recently_post': recently_post,
            'recently_comment': recently_comment,
            'tags': Tag.objects.all(),
        }
        context.update(kwargs)

        return super(CommonContextMixin, self).get_context_data(**context)
