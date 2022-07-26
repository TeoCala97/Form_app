
from logging import PlaceHolder
from django import forms
from .models import forms_api


class Formulario(forms.ModelForm):
    class Meta:
        model =  forms_api
        fields = '__all__'
        widgets = {'Fecha_envio':forms.DateTimeInput(attrs={'type': 'date','class':'form-control-sm'}),
        'Nombre_campo':forms.TextInput(attrs={'PlaceHolder':'Ingrese el Nombre del Campo'}),
        'Email':forms.EmailInput(attrs={'PlaceHolder':'Ingrese el Su Correo Electrónico'}),
        'Nombre_campanha':forms.EmailInput(attrs={'PlaceHolder':'Ingrese el Nombre de la Campaña'}),
        'Prioridad':forms.EmailInput(attrs={'PlaceHolder':'Ingrese la prioridad'}),
        'Table_name':forms.EmailInput(attrs={'PlaceHolder':'Ingrese el valor del Campo'}),
        'Valor_Campo':forms.EmailInput(attrs={'PlaceHolder':'Ingrese el valor del Campo'}),
        }
   
