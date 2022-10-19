from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,request
from django.shortcuts import redirect    
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,TemplateView 
from Form.models import Query, forms_api

class HomePage(LoginView):
    template_name =  'registration/login.html'
    
class DashView(TemplateView):
    template_name = 'core/dash.html'
    model = forms_api

    def get_data(self):
        camp = self.model.objects.all()
        return camp
    
    def get_context_data(self, *args, **kwargs):
        context = super(DashView, self).get_context_data(*args, **kwargs)
        context['camp'] = self.get_data()
        return context

class LockView(LoginView):
    template_name =  'registration/lock.html'

class MainView(TemplateView):
    template_name =  'core/maintenance.html'