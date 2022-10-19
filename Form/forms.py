from django import forms
from .models import forms_api,Query

#%% Admin Campañas
class Formulario(forms.ModelForm):
    class Meta:
        model =  forms_api
        fields = '__all__'
        widgets = {'Nombre_campanha':forms.TextInput(attrs={'class':'form-control'}),
                    'Marca':forms.Select(attrs={'class':'form-control'}),
                    'Canal':forms.Select(attrs={'class':'form-control'}),
                    'Fecha_envio':forms.DateTimeInput(attrs={'type': 'date','class':'form-control'}),
                    'Email':forms.EmailInput(attrs={'class':'form-control'}),
                    'Tipo_usuario':forms.Select(attrs={'class':'select2 form-control select2-multiple'}),
                    'Table_name':forms.TextInput(attrs={'class':'form-control'}),
                    'Nombre_campo':forms.TextInput(attrs={'class':'form-control'}),
                    'Valor_Campo':forms.TextInput(attrs={'class':'form-control'}),
                    'Prioridad':forms.NumberInput(attrs={'class':'form-control'})
                    }
#%% Admin Provisiones
class Provisiones(forms.ModelForm):

    class Meta:
        model = Query
        fields = '__all__'
        widgets = {'qname':forms.TextInput(attrs={'class':'form-control'}),
                    'select':forms.Select(attrs={'type': 'select','class':'form-control'}),
                    'fecha':forms.DateTimeInput(attrs={'type': 'date','class':'form-control'}),}   