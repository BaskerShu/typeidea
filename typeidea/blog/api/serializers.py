# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers, pagination

from blog.models import Post, Category, Tag


class PostSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name'
    )
    tag = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='name'
    )
    created_time = serializers.DateTimeField(
        format('%Y-%m-%d %H:%M:%S')
    )

    class Meta:
        model = Post
        fields = ('url', 'title', 'desc', 'category',
                 'tag', 'pv', 'uv', 'created_time', )


class PostDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name'
    )
    tag = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='name'
    )
    created_time = serializers.DateTimeField(
        format('%Y-%m-%d %H:%M:%S')
    )

    class Meta:
        model = Post
        fields = ('url', 'title', 'desc', 'category',
                  'tag', 'pv', 'uv', 'created_time',
                  'content', 'html')


class CategorySerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(
        format('%Y-%m-%d %H:%M:%S')
    )

    class Meta:
        model = Category
        fields = ('url', 'name', 'get_status_display', 'is_nav', 'created_time', )


class CategoryDetailSerializer(serializers.ModelSerializer):
    post_set = serializers.SerializerMethodField('paginated_posts')
    created_time = serializers.DateTimeField(
        format('%Y-%m-%d %H:%M:%S')
    )

    def paginated_posts(self, obj):
        posts = obj.post_set.all()
        paginator = pagination.PageNumberPagination()
        page = paginator.paginate_queryset(posts, self.context['request'])
        serializer = PostSerializer(page, many=True, read_only=True, context={'request': self.context['request']})

        return {
            'results': serializer.data,
            'previous': paginator.get_previous_link(),
            'next': paginator.get_next_link(),
        }

    class Meta:
        model = Category
        fields = ('url', 'name', 'get_status_display',
                  'is_nav', 'created_time', 'post_set', )


class TagSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(
        format('%Y-%m-%d %H:%M:%S')
    )

    class Meta:
        model = Tag
        fields = ('url', 'name', 'get_status_display', 'created_time', )


class TagDetailSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(
        format('%Y-%m-%d %H:%M:%S')
    )
    post_set = serializers.SerializerMethodField('paginated_posts')

    def paginated_posts(self, obj):
        posts = obj.post_set.all()
        paginator = pagination.PageNumberPagination()
        page = paginator.paginate_queryset(posts, self.context['request'])
        serializer = PostSerializer(page, many=True, read_only=True, context={'request': self.context['request']})

        return {
            'results': serializer.data,
            'previous': paginator.get_previous_link(),
            'next': paginator.get_next_link(),
        }

    class Meta:
        model = Tag
        fields = ('url', 'name', 'get_status_display', 'created_time', 'post_set')
