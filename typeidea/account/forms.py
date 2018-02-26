# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from PIL import Image
from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile
from typeidea.widget import CustomImageFileInput

logger = logging.getLogger(__name__)


class LoginForm(AuthenticationForm):
    captcha = CaptchaField()


class RegisterForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', )


class ProfileForm(forms.ModelForm):
    x = forms.FloatField(required=False, widget=forms.HiddenInput())
    y = forms.FloatField(required=False, widget=forms.HiddenInput())
    width = forms.FloatField(required=False, widget=forms.HiddenInput())
    height = forms.FloatField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Profile
        fields = ['user', 'avatar', 'location', 'blog_site', 'x', 'y', 'width', 'height']
        widgets = {'user': forms.HiddenInput(), 'avatar': CustomImageFileInput, }

    def save(self):
        logger.debug("picture is come")
        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        width = self.cleaned_data.get('width')
        height = self.cleaned_data.get('height')

        profile = super(ProfileForm, self).save()
        if any([x, y, width, height]):
            crop_image(profile, (x, y, width + x, height + y), (100, 100))

        return profile


def crop_image(profile, crop_position, crop_size):
    image = Image.open(profile.avatar)
    cropped_image = image.crop(crop_position)
    resized_image = cropped_image.resize(crop_size, Image.ANTIALIAS)
    resized_image.save(profile.avatar.path, 'PNG')
