from distutils.command.upload import upload
import imp
from webbrowser import get
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
import json
from Form.forms import Formulario
from functions.functions import GCP_gestor
from Camp.models import Camp
from django.http import QueryDict
# Create your views here.

class FormView(HttpRequest):

    def formu_index(request):
        formulario = Formulario()
        Campos = Camp()
        if request.method == 'POST':
            formulario = Formulario(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                formu = dict(request.POST)
                formu['key_lecture']=int(1)
                GCP_gestor.connect_client('sod-co-bi-sandbox','sod-co-bi-sandbox-campanhas')  
                jsondata_post = 'cfg_audiencia_parametros_campanhas.json'
                print(formu)
                GCP_gestor.post_form(jsondata_post, formu)
                File = GCP_gestor.get_form()
                print(File)
                File['key_lecture']=int(0)
                jsondata_get = 'post_data.Sjson'
                GCP_gestor.post_form(jsondata_get, File)
                print(File)
            return render(request,'Form/camp.html', {'ID': File['Campanha_id'], 'Nombre_C': File['Nombre_campania'], 'N_registros': File['N_registros']})
        return render(request,'Form/form.html',{'form':formulario})