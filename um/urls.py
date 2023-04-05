from django.urls import path
from . import views

app_name = "um"
urlpatterns = [
    path(
        "subscription/<pk>/",
        views.package_type_subscription_view,
        name="package_type_subscription",
    ),
    path("search", views.SearchView.as_view(), name="search_view"),
]
