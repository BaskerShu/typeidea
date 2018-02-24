# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

register = template.Library()


@register.inclusion_tag('comment/block.html', takes_context=True)
def comment_block(context):
    return {
        'request': context['request'],
        'comment_form': context['comment_form'],
        'comment_list': context['comment_list'],
    }
