from django.shortcuts import render

from django.views.generic import TemplateView

from config.template_name import HOME_TEMPLATE, ABOUT_TEMPLATE


class HomeView(TemplateView):
    template_name = HOME_TEMPLATE


class AboutView(TemplateView):
    template_name = ABOUT_TEMPLATE