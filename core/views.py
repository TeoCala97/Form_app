from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,request
from django.shortcuts import redirect    
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

class HomePage(LoginView):
    template_name =  'registration/login.html'
    
