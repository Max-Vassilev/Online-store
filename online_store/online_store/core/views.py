from django.shortcuts import render
from django.views import generic as views


class BasePageView(views.TemplateView):
    template_name = 'core/base.html'