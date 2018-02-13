# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm, RegisterForm


class RegisterView(FormView):
    template_name = 'account/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('profile_home')

    def post(self, request, *args, **kwargs):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()

            return HttpResponseRedirect(self.get_success_url())


@login_required
def profile_home(request):
    return HttpResponseRedirect(
        reverse('profile', args=[request.user.username])
    )


class ProfileView(FormView):
    template_name = 'account/profile.html'
    form_class = ProfileForm
