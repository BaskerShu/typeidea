# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from captcha.fields import CaptchaField
from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile


class LoginForm(AuthenticationForm):
    captcha = CaptchaField()


class RegisterForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email',)


class ProfileForm(forms.ModelForm):
    avatar = ProcessedImageField(spec_id='account:profile:avatar',
                                 processors=[ResizeToFill(100, 50)],
                                 format='JPEG',
                                 options={'quality': 60})

    class Meta:
        model = Profile
        fields = ['user', 'avatar', 'location', 'birthdate']
        widgets = {'user': forms.HiddenInput()}
