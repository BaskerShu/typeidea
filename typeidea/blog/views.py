# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.cache import cache
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Post, Tag
from typeidea.views import CommentShowMixin, CommonContextMixin


class ListPostsView(CommonContextMixin, ListView):
    model = Post
    template_name = 'blog/list.html'
    paginate_by = 3
    context_object_name = 'posts'


class IndexView(ListPostsView):
    def get_queryset(self):
        query = self.request.GET.get('query')
        queryset = super(IndexView, self).get_queryset()
        if query:
            queryset = queryset.filter(title__icontains=query)

        return queryset

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('query')

        return super(IndexView, self).get_context_data(query=query, isIndex=True)


class CategoryView(ListPostsView):
    def get_queryset(self):
        queryset = super(CategoryView, self).get_queryset()
        cate_id = self.kwargs.get('category_id', 1)  # 获得从url传递的category_id
        posts = queryset.filter(category_id=cate_id, status=1)

        return posts

    def get_context_data(self, **kwargs):
        cate_id = self.kwargs.get('category_id', 1)  # 获得从url传递的category_id

        return super(CategoryView, self).get_context_data(cate_id=cate_id)


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

    def get_context_data(self, **kwargs):
        tag_id = self.kwargs.get('tag_id')

        return super(TagView, self).get_context_data(tag_id=tag_id)


class AuthorView(ListPostsView):
    def get_queryset(self):
        posts = super(AuthorView, self).get_queryset()
        author_id = self.kwargs.get('author_id', 1)
        if author_id:
            posts = posts.filter(owner_id=author_id)

        return posts

    def get_context_data(self, **kwargs):
        author_id = self.kwargs.get('author_id')

        return super(AuthorView, self).get_context_data(author_id=author_id)


class PostView(CommonContextMixin, CommentShowMixin, DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/detail.html'
    pk_url_kwarg = 'post_id'

    def get(self, request, *args, **kwargs):
        # 先进行父类的get操作,是因为self.object只有在进行完get操作后才会拿到
        response = super(PostView, self).get(request, *args, **kwargs)
        self.update_pv_uv()

        return response

    def update_pv_uv(self):
        session_id = self.request.COOKIES.get('sessionid')
        path = self.request.path
        if not session_id:
            return
        pv_key = 'pv:%s:%s' % (session_id, path)
        uv_key = 'uv:%s:%s' % (session_id, path)

        if not cache.get(pv_key):
            cache.set(pv_key, 1, 60)
            self.object.update_pv()
        elif not cache.get(uv_key):
            cache.set(uv_key, 1, 60 * 60 * 24)
            self.object.update_uv()
