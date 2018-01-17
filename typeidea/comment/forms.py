# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        max_length=500,
        label="内容",
        widget=forms.widgets.Textarea(attrs={'rows': 6, 'cols': 60})
    )

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError("长度太短了")

        return content

    class Meta:
        model = Comment
        fields = ['nickname', 'email', 'website', 'content']
