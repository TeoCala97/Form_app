from ast import For
from multiprocessing import context
from string import Template
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from Form.forms import Formulario
from Form.models import Query, forms_api

# Create your views here.
class TableCampView(TemplateView):
    template_name = 'Tables/tablecamp.html' 
    model = forms_api

    def get_data(self):
        camp = self.model.objects.all()
        return camp
    
    def get_context_data(self, *args, **kwargs):
        context = super(TableCampView, self).get_context_data(*args, **kwargs)
        context['camp'] = self.get_data()
        return context

    

class TableProvView(TemplateView):
    template_name = 'Tables/tableprov.html' 
    model = Query

    def get_data(self):
        prov = self.model.objects.all()
        return prov
    
    def get_context_data(self, *args, **kwargs):
        context = super(TableProvView, self).get_context_data(*args, **kwargs)
        context['prov'] = self.get_data()
        return context
    

class TableRepoView(TemplateView):
    template_name = 'Tables/tablerepor.html' 