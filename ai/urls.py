from django.urls import path
from django.views.generic import TemplateView
from . import views



urlpatterns = [
    path('generator/', views.generator_page, name='generator_page'),
    path('generator/process/', views.generator_handler, name='generator_handler'),
    # path('', views.index),
    # path('', views.index),
    # path('', views.index),
]
