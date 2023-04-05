from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls", namespace="pages")),
    path("ai/", include("ai.urls", namespace="ai")),
    # path('accounts/', include('accounts.urls', namespace='accounts')),
    path("accounts/", include("allauth.urls")),
    path("um/", include("um.urls", namespace="um")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
