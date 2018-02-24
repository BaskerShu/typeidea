# -*- coding: utf-8 -*-
from markdownx.widgets import AdminMarkdownxWidget
from django.forms.widgets import ClearableFileInput


class CustomAdminMarkdownxWidget(AdminMarkdownxWidget):
    class Media:
        extend = False
        css = {
            'all': [
                'css/markdownx.css',
                'css/markdown-skin/desert.css'
            ]
        }
        js = [
            'markdownx/js/markdownx{}.js'.format(''),
            'js/prettify.js',
            'js/markdownx-widget.js',
        ]


class CustomImageFileInput(ClearableFileInput):
    template_name = 'customforms/custom_image.html'
