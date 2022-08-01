
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from Form.forms import Formulario
from functions.functions import GCP_gestor
from Camp.models import Camp
from django.views.generic.edit import FormView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

class StaffRequieredMixin(object):
    """Este Mixin requiere que el usuario sea miembro del Staff"""
    def dispatch(self, request,*arg,**kwarg):
        return super(StaffRequieredMixin,self).dispatch(request,*arg,**kwarg)



class FormView(FormView):
    template_name = 'Form/form.html'
    form_class = Formulario
    success_url = reverse_lazy('campaña')

    def post(self,request,*args,**kwargs):
        formulario = Formulario()
        if request.method == 'POST':
            formulario = Formulario(data=request.POST)
            if formulario.is_valid():
                print(request.POST)
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
                jsondata_get = 'post_data.json'
                GCP_gestor.post_form(jsondata_get, File)
                print(File)
            return render(request,'Form/camp.html', {'ID': File['Campanha_id'], 'Nombre_C': File['Nombre_campania'], 'N_registros': File['N_registros']})
            # return reverse_lazy('campaña')

    def form_valid(self, form):
        return super().form_valid(form)