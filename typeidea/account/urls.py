# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib.auth.views import LoginView

from .forms import LoginForm
from .views import profile_home, ProfileView, RegisterView

urlpatterns = [
    url(r'login/$',
        LoginView.as_view(
            template_name='account/login.html',
            form_class=LoginForm,
        ),
        name='login'),
    url(r'register/$', RegisterView.as_view(), name='register'),
    url(r'profile/home/$', profile_home, name='profile_home'),
    url(r'profile/home/(?P<username>\w+)/$', ProfileView.as_view(), name='profile'),
]
