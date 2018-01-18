# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.views.generic import TemplateView

from .forms import CommentForm


class CommentView(TemplateView):
    template_name = 'comment/result.html'
    http_method_names = ['post', ]

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        target = request.POST.get('target')
        if comment_form.is_valid():
            success = True
            comment = comment_form.save(commit=False)
            comment.target = target
            comment.save()

            return redirect(target)
        else:
            success = False

        context = {
            'success': success,
            'comment_form': comment_form,
            'target': target,
        }
        return self.render_to_response(context)
