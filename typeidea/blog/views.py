# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Post, Tag, Category
from config.models import SideBar
from comment.models import Comment


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
        }
        context.update(kwargs)

        return super(CommonContextMixin, self).get_context_data(**context)


class ListPostsView(CommonContextMixin, ListView):
    model = Post
    template_name = 'blog/list.html'
    paginate_by = 2
    context_object_name = 'posts'


class IndexView(ListPostsView):
    pass


class CategoryView(ListPostsView):
    def get_queryset(self):
        queryset = super(CategoryView, self).get_queryset()
        cate_id = self.kwargs.get('category_id', 1)  # 获得从url传递的category_id
        posts = queryset.filter(category_id=cate_id, status=1)

        return posts


class TagView(ListPostsView):
    def get_queryset(self):
        tag_id = self.kwargs.get('tag_id')
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            posts = []
        else:
            posts = tag.post_set.filter(status=1)

        return posts


class PostView(CommonContextMixin, DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/detail.html'
    pk_url_kwarg = 'post_id'
