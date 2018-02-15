# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile


class LoginForm(AuthenticationForm):
    captcha = CaptchaField()


class RegisterForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'location', 'birthdate']
