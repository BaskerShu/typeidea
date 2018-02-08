# -*- coding: utf-8 -*-

from dal import autocomplete
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from markdownx.fields import MarkdownxFormField
from markdownx.widgets import AdminMarkdownxWidget
from simditor.widgets import SimditorWidget

from .models import Category, Tag
from .widget import CustomAdminMarkdownxWidget


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
    content = forms.CharField(widget=CustomAdminMarkdownxWidget())
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=autocomplete.ModelSelect2(url='category-autocomplete'),
        label='分类',
    )
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
        label='标签',
    )
