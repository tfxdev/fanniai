from django.urls import path, include
from django.views.generic import TemplateView

from config.template_name import ABOUT_TEMPLATE
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', TemplateView.as_view(template_name=ABOUT_TEMPLATE), name='about' ),

    # path('', views.index),
    # path('', views.index),
    # path('', views.index),
    # path('', views.index),
]



# 1. A library or catalog of comics: Users should be able to browse through a list of all the comics that are available in the app. Each comic should have a cover image, a title, and a brief description. (DONE)
# 2. A reader: Users should be able to read the comics in the app, with features such as zooming in and out, panning, and navigating between pages or “Guided View” (DONE)

# 3. A notification system: Users should be able to receive notifications when new comics are added, or when new chapters are released. (DONE)
# 4. Comic organization: The comics should be organized in Series/Chapter manner for easy access and reading for the users. (DONE)

# 5. Everything should be revised and ready to publish (DONE)
# 6. Publish (DONE)