from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import SignupForm

# Create your views here.

class SignupView(CreateView):
         
         form_class = SignupForm
         
         template_name = 'registration/signup.html'
         
         success_url = reverse_lazy('login')
         

class CustomLoginView(LoginView):
    
         template_name = 'registration/login.html'            