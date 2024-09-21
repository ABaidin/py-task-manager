from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView

from .forms import LoginForm, RegistrationForm


class CustomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = "accounts/login.html"

    def form_valid(self, form):
        remember_me = form.cleaned_data.get("remember_me")
        if remember_me:
            self.request.session.set_expiry(settings.SESSION_COOKIE_AGE)
        else:
            self.request.session.set_expiry(0)

        login(self.request, form.get_user())
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse("tasks:task-list")


class CustomRegisterView(CreateView):
    form_class = RegistrationForm
    template_name = "accounts/register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse("tasks:task-list")
