# -*- coding: utf-8 -*-

from markdownx.widgets import AdminMarkdownxWidget


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
            'markdownx/js/markdownx{}.js'.format('.min'),
            'js/prettify.js',
            'js/markdownx-widget.js',
        ]
