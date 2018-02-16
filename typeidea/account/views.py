# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, Http404
from django.views.generic import FormView
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm, RegisterForm


class RegisterView(FormView):
    template_name = 'account/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('profile_home')

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())


@login_required
def profile_home(request):
    return HttpResponseRedirect(
        reverse('profile', args=[request.user.username])
    )


class ProfileView(FormView):
    template_name = 'account/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')
        if username != request.user.username:
            raise Http404('当前页面不存在')
        return self.render_to_response(self.get_context_data())

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(instance=self.request.user.profile, **self.get_form_kwargs())
