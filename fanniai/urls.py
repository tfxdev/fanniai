from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('ai/', include('ai.urls', namespace='ai')),
    # path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('allauth.urls')),
    path('um/', include('um.urls')),
]
