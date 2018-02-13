# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='用户')
    avatar = models.ImageField(upload_to="avatar/", verbose_name='头像')
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if created:
        return Profile.objects.create(user=instance)
    else:
        instance.profile.save()
