import re
from django.shortcuts import render
from .models import Camp
from functions.functions import GCP_gestor

# Create your views here.
class CampView:

    def Camp_get(request):
        files = GCP_gestor.get_form
        camp = Camp()
        return render(request,'Camp/camp.html',{'camp':camp})
        