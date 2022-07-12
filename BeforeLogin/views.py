from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, FormView
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import View


# Create your views here.

class UserRegistrationView(FormView):
    template_name = 'registration.html'
    form_class = UserRegistrationForm
    success_url = '/login'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(UserRegistrationView, self).form_valid(form)


class UserLoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(self.request, user)
                return HttpResponseRedirect(reverse_lazy('afterlogin:index'))

        return HttpResponseRedirect(reverse_lazy('beforelogin:login'))


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('beforelogin:login'))
