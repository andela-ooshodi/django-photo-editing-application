from django.shortcuts import render
from django.views.generic import TemplateView


class SigninView(TemplateView):
    template_name = 'photoapp/signin.html'


class HomeView(TemplateView):
    template_name = 'photoapp/home.html'
