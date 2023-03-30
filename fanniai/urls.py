from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('ai/', include('ai.urls')),
<<<<<<< HEAD
    path('accounts/', include('accounts.urls', namespace='accounts')),
=======
    path('um/', include('um.urls')),
>>>>>>> 6c7594aacacf9d56e505ad8cb11ac014c8624027
]
