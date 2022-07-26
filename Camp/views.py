from msilib.schema import ListView
import re
from django.shortcuts import render
from .models import Camp
from functions.functions import GCP_gestor
from django.views.generic import TemplateView
import json



# Create your views here.
class CampView(TemplateView):
    template_name = 'Camp/camp.html'
    model = Camp
    
    def get(self,request,*args,**kwargs):
        # with open("post_data.json","r") as j:
        #     datos=json.load(j)
        # print(datos)
        # camp = Camp.objects.create(data=datos)
        # camp.save()
        File = GCP_gestor.get_form()
        print(File)
        File['key_lecture']=int(0)
        jsondata_get = 'post_data.json'
        GCP_gestor.post_form(jsondata_get, File)
        print(File)
        if File['key_lecture'] == int(0):
            return render(request,self.template_name,{'ID': File['Campanha_id'], 'Nombre_C': File['Nombre_campania'], 'N_registros': File['N_registros']})
        else:
            return render(request,self.template_name,{'ID': '?' , 'Nombre_C': '?', 'N_registros': '?'})
        


    
        
