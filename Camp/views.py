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
        if request.user:
            camp = Camp()
            with open("post_data.json","r") as j:
                datos=json.load(j)
            print(datos)
            # camp.Campanaha_id = datos['Campanha_id']
            # camp.Nombre_campanha = datos['Nombre_campania']
            # camp.N_registro = datos['N_registros']
            # camp.save(update_fields=["Campanaha_id"]) 
            # camp.save(update_fields=["Nombre_campanha"]) 
            # camp.save(update_fields=["N_registro"]) 
            return render(request,self.template_name,{'ID': datos['Campanha_id'], 'Nombre_C': datos['Nombre_campania'], 'N_registros': datos['N_registros']})
        

    
        
