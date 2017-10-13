# -*- coding: utf-8 -*-

from django import forms


class CommentAdminForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, max_length=2000)
