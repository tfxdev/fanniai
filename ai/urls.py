from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "ai"

urlpatterns = [
    path("generator/", views.generator_page, name="generator_page"),
    path("generator/process/", views.generator_handler, name="generator_handler"),
]
