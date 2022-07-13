from msilib.schema import ListView
import re
from django.shortcuts import render
from .models import Camp
from functions.functions import GCP_gestor as gcp
from django.views.generic import TemplateView
import json



# Create your views here.
class CampView(TemplateView):
    template_name = 'Camp/camp.html'

    def get(self,request,*args,**kwargs):
        with open("post_data.json","r") as j:
            datos=json.load(j)
        print(datos)
        if datos['key_lecture'] == int(0):
            return render(request,self.template_name,{'ID': datos['Campanha_id'], 'Nombre_C': datos['Nombre_campania'], 'N_registros': datos['N_registros']})
        else:
            return render(request,self.template_name,{'ID': '?' , 'Nombre_C': '?', 'N_registros': '?'})
        

    
        
