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
    Camp = Camp()
    
    def get(self,request,*args,**kwargs):
        with open("post_data.json","r") as j:
            datos=json.load(j)
        print(datos)
        camp = Camp.objects.create(data=datos)
        camp.save()
        if Camp.datos['key_lecture'] == int(0):
            return render(request,self.template_name,{'ID': Camp.datos['Campanha_id'], 'Nombre_C': Camp.datos['Nombre_campania'], 'N_registros': Camp.datos['N_registros']})
        else:
            return render(request,self.template_name,{'ID': '?' , 'Nombre_C': '?', 'N_registros': '?'})
        


    
        
