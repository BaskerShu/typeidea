# -*- coding: utf-8 -*-

from django import forms


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
    html = forms.CharField(widget=forms.Textarea, label='html内容', help_text="markdown格式的内容经过转换成为html内容", required=False)
