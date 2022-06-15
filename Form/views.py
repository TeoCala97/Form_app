from distutils.command.upload import upload
from webbrowser import get
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
import json

from Form.forms import Formulario

# Create your views here.
class FormView(HttpRequest):

    def formu_index(request):
        formulario = Formulario()
        if request.method == 'POST':
            formulario = Formulario(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                formu = json.dumps(request.POST)
                print(formu)
            return redirect(reverse("formulario")+"?ok" )
        return render(request,'Form/form.html',{'form':formulario})


