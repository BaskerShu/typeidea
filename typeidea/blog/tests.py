# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.test import TestCase
from django.db import connection
from django.db.models import Q
from django.db.models import F
from django.db.models import Count
from django.db.models import Sum
from django.test.utils import override_settings
from pprint import pprint as pp

from .models import Category


class TestCategory(TestCase):
    # @override_settings(DEBUG=True)
    def setUp(self):
        self.user = User.objects.create_user('BaskerShu', 'yangshuzhi@outlook.com', 'password')
        Category.objects.bulk_create([
            Category(name='cate_%s' % i, owner=self.user) for i in range(10)
        ])

    # @override_settings(DEBUG=True)
    def test_filter(self):
        categories = Category.objects.filter(
            (Q(id=1) | Q(id=2))
        )

        category = Category.objects.filter(id=1).update(status=F('status') + 1)
        user = User.objects.annotate(cate_sum=Sum('category__status')).get(username='BaskerShu')

    @override_settings(DEBUG=True)
    def test_values(self):
        categories = Category.objects.only('name')

        user = User.objects.get(username='BaskerShu').category_set.all()
        print (user)

        pp(connection.queries)
