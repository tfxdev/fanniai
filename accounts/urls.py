from django.urls import path
from. import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('forget_password/', views.ForgetPassword.as_view(), name='forget'),
]
