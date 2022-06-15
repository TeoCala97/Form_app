from distutils.command.upload import upload
from webbrowser import get
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
import json
from Form.forms import Formulario


from google.cloud import pubsub_v1
from google.cloud import bigquery
from google.cloud import storage
# from google.oauth2 import service_account


client = bigquery.Client(project='sod-co-bi-sandbox')
client_storage= storage.Client(project='sod-co-bi-sandbox')
bucket = client_storage.get_bucket('crm_symphony_cfg_co')

# Create your views here.
class FormView(HttpRequest):

    def formu_index(request):
        formulario = Formulario()
        if request.method == 'POST':
            formulario = Formulario(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                formu = json.dumps(request.POST)
                blob = bucket.blob(formu)
                blob.upload_from_filename('cfg_sp_audiencia_sod_mo_sku.json')
            return redirect(reverse("formulario")+"?ok" )
        return render(request,'Form/form.html',{'form':formulario})


