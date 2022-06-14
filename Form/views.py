from distutils.command.upload import upload
from webbrowser import get
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from .forms import Formulario
from django.core.files.storage import FileSystemStorage

# Create your views here.
def formu(request):
    formulario = Formulario()
    if request.method == 'POST':
        formulario = Formulario(data=request.POST)
        if formulario.is_valid():
            Nombre_campañia = request.POST.get('Nombre_campañia','')
            Marca = request.POST.get('Marca','')
            Canal = request.POST.get('Canal','')
            fecha_envia = request.POST.get('Fecha_envia ','')
            Email = request.POST.get('Email','')
            Camp = request.POST.get('Camp','')
            Prioridad = request.POST.get('Camp','')
            return JsonResponse(request.POST)
    return render(request,'Form/form.html',{'form':formulario})
