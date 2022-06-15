from django import forms
from .models import forms_api


class Formulario(forms.ModelForm):
    class Meta:
        model =  forms_api
        fields = '__all__'
        widgets = {'Fecha_envia':forms.DateTimeInput(attrs={'type': 'date','class':'form-control-sm'})}
