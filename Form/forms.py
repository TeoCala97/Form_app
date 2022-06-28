from django import forms
from .models import forms_api


class Formulario(forms.ModelForm):
    class Meta:
        model =  forms_api
        fields = '__all__'
        widgets = {'Fecha_envio':forms.DateTimeInput(attrs={'type': 'date','class':'form-control-sm'})}

    def __init__(self,*arg,**kwarg):
        super().__init__(*arg,**kwarg)
        if self.instance.Table_name:
            self.fields['Valor_Campo'].widget.attrs.update({'disabled': True})

