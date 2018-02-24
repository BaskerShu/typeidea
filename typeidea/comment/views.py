# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.views.generic import TemplateView

from .forms import CommentForm


class CommentView(TemplateView):
    template_name = "comment/result.html"
    http_method_names = ['post', ]

    def form_valid(self, form, target):
        comment = form.save(commit=False)
        comment.target = target
        comment.owner = self.request.user
        comment.save()
        return redirect(target + "#comment")

    def form_invalid(self, form, target):
        context = {
            'form': form,
            'target': target,
        }
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        target = self.request.POST.get('target')
        if comment_form.is_valid():
            return self.form_valid(comment_form, target)
        else:
            return self.form_invalid(comment_form, target)
