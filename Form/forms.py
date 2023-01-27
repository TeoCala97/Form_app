from django import forms
from .models import forms_api


class Formulario(forms.ModelForm):
    class Meta:
        model =  forms_api
        fields = '__all__'
        widgets =  {'Nombre_campanha':forms.TextInput(attrs={'class':'form-control'}),
                    'Categoria':forms.TextInput(attrs={'class':'form-control'}),
                    'Marca':forms.Select(attrs={'class':'form-control'}),
                    'Canal':forms.Select(attrs={'class':'form-control'}),
                    'Fecha_envio':forms.DateTimeInput(attrs={'type': 'date','class':'form-control'}),
                    'Email':forms.EmailInput(attrs={'class':'form-control'}),
                    'Tipo_usuario':forms.Select(attrs={'class':'form-control'}),
                    'Table_name':forms.TextInput(attrs={'class':'form-control'}),
                    'Nombre_campo':forms.TextInput(attrs={'class':'form-control'}),
                    'Valor_Campo':forms.TextInput(attrs={'class':'form-control'}),
                    'Prioridad':forms.NumberInput(attrs={'class':'form-control'}),
        }

    def __init__(self,*arg,**kwarg):
        super().__init__(*arg,**kwarg)
        if self.instance.Table_name:
            self.fields['Valor_Campo'].widget.attrs.update({'disabled': True})

