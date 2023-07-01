from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "mainapp/index.html"


class LoginView(TemplateView):
    template_name = "mainapp/login.html"


class RequestView(TemplateView):
    template_name = "mainapp/request.html"


class ResponseView(TemplateView):
    template_name = "mainapp/response.html"


