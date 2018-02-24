# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponseRedirect, Http404
from django.views.generic import FormView, TemplateView
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


from .forms import RegisterForm, UserForm, ProfileForm
from typeidea.views import CommonContextMixin


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


@login_required
def crop_image(request):
    if request.method == "POST":
        profile_form = ProfileForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if profile_form.is_valid():
            profile = profile_form.save()
            data = {
                'image_url': profile.avatar.url,
                'random': random.random(),
            }
            return JsonResponse(data)
    return Http404("error")


class ProfileView(CommonContextMixin, TemplateView):
    template_name = 'account/profile.html'
    form_class = ProfileForm

    def form_valid(self, user_form, profile_form):
        user_form.save()
        profile_form.save()
        return HttpResponseRedirect(reverse('profile_home'))

    def form_invalid(self, user_form, profile_form):
        return self.render_to_response(self.get_context_data(user_form=user_form, profile_form=profile_form))

    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')
        if username != request.user.username:
            raise Http404('当前页面不存在')
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        user_form = UserForm(data=self.request.POST, instance=self.request.user)
        profile_form = ProfileForm(data=self.request.POST, files=self.request.FILES, instance=self.request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            return self.form_valid(user_form, profile_form)
        else:
            return self.form_invalid(user_form, profile_form)

    def get_context_data(self, *args, **kwargs):
        if 'user_form' not in kwargs and 'profile_form' not in kwargs:
            kwargs.update({
                'user_form': UserForm(instance=self.request.user),
                'profile_form': ProfileForm(instance=self.request.user.profile),
            })
        return super(ProfileView, self).get_context_data(**kwargs)
