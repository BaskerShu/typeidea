# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from typeidea.storage import OverwriteStorage


def user_avatar_path(instance, filename):
    return "avatar/{0}/{1}".format(instance.user.username, 'avatar.png')


class Profile(models.Model):
    LOCATION_ITEMS = (
        (0, '保密'),
        (1, '北京市'), (2, '天津市'), (3, '上海市'), (4, '重庆市'),
        (5, '河北省'), (6, '山西省'), (7, '辽宁省'), (8, '吉林省'),
        (9, '黑龙江省'), (10, '江苏省'), (11, '浙江省'), (12, '安徽省'),
        (13, '福建省'), (14, '江西省'), (15, '山东省'), (16, '河南省'),
        (17, '湖北省'), (18, '湖南省'), (19, '广州省'), (20, '海南省'),
        (21, '四川省'), (22, '贵州省'), (23, '云南省'), (24, '陕西省'),
        (25, '甘肃省'), (26, '青海省'), (27, '台湾省'), (28, '内蒙古自治区'),
        (29, '广西壮族自治区'), (30, '西藏自治区'), (31, '宁夏回族自治区'), (32, '新疆维吾尔自治区'),
        (33, '香港特别行政区'), (34, '澳门特别行政区'),
    )

    user = models.OneToOneField(User, verbose_name='用户')
    avatar = models.ImageField(upload_to=user_avatar_path, default="avatar/default/avatar.png", storage=OverwriteStorage(), verbose_name="头像")
    location = models.IntegerField(default=0, choices=LOCATION_ITEMS, verbose_name="位置")
    blog_site = models.URLField(max_length=30, blank=True, verbose_name="博客地址")


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if created:
        return Profile.objects.create(user=instance)
    else:
        instance.profile.save()
