import re
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login,logout,get_user_model
from django.core.cache import cache
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import TemplateView

from config.template_name import FORGET_TEMPLATE, LOGIN_TEMPLATE, REGISTRATION_TEMPLATE


#! User model
UserModel = get_user_model()


#! User login view
class LoginView(View):
    def get(self,request):
        #? If user is already login then redirect to home page
        # If user is already login
        if request.user.is_authenticated:
            return redirect('core:home')
        
        #? Set cache next url. If any authenticated required hit unauthorized user
        if request.method == 'GET':
            cache.set('next', request.GET.get('next', None))

        return render(request, LOGIN_TEMPLATE)

    def post(self,request):
        #? If user is already login
        # If user is already login
        if request.user.is_authenticated:
            return redirect('home:home')
        
        #? User email and password taken from login page and verify user
        username = request.POST.get('email')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        user = authenticate(request,username=username, password=password)

        #? If User verification successfully then redirect to home page or next url page
        if user is not None:
            login(request,user)
            if remember == 'on':
                request.session.set_expiry(60*60*24*7)
            else:
                request.session.set_expiry(0)

            next_url = cache.get('next')
            if next_url:
                cache.delete('next')
                return HttpResponseRedirect(next_url)

            return redirect('home:home')
        
        #? If User verification failed then redirect to login page with error message
        else:
            context = {'email': username}
            messages.error(request, 'Invalid email or password')
            return render(request,LOGIN_TEMPLATE, context)

#! Create your views here.
class RegistrationView(View):
    def get(self,request):
        # If user is already login
        if request.user.is_authenticated:
            return redirect('home:home')
        return render(request, REGISTRATION_TEMPLATE)

    def post(self,request):
        # If user is already login
        if request.user.is_authenticated:
            return redirect('home:home')

        #? User sing up data
        name = request.POST.get('fullname').title()
        email = request.POST.get('email')
        password = request.POST.get('password')

        context={
            'data':request.POST,
            'has_error': False
        }

        #? Validation for email address
        EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if email and not re.match(EMAIL_REGEX, email):
            messages.error(request, 'Invalid email address')
            context['has_error'] = True
        
        #? Check database is email exists or not
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email address already exists')
            context['has_error'] = True
        
        #? sent error message
        if context['has_error']:
            context['name'] = name
            context['email'] = email
            context['password'] = ''
            return render(request,REGISTRATION_TEMPLATE,context)
        
        # Create user and save user in database
        user = User.objects.create_user(username = email, email = email)
        user.set_password(password)
        user.is_active = True
        user.first_name = name
        user.save()

        messages.info(request, 'Account created successfully')

        return redirect('account:login')


#! Account Logout views
class LogoutView(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        return redirect('home:home') # Logout successful and redirect to home page


class ForgetPassword(TemplateView):
    template_name = FORGET_TEMPLATE