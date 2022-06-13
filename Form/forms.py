from cProfile import label
from django import forms
from django.forms.widgets import NumberInput


class Formulario(forms.Form):
    MARCAS = [
        ("", ""),
        ("HC", "Homecenter"),
        ("CT", "Constructor"),
    ]
    CANAL = [
        ("", ""),
        ("EMAIL", "Email"),
        ("CELULAR", "Celular"),
    ]
    CAMPOS = [
        ("", ""),
        ("ONLINE", "ONLINE"),
        ("HARD", "HARD"),
        ("SOFT", "SOFT"),
        ("TODOS", "TODOS"),
        ("ACABADOS", "ACABADOS"),
    ]
    Nombre_campania = forms.CharField(label="Nombre de Campaña", required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    Marca = forms.ChoiceField(choices=MARCAS,widget=forms.Select(attrs={'class':'form-control'}))
    Canal = forms.ChoiceField(choices=CANAL,widget=forms.Select(attrs={'class':'form-control'}))
    Fecha_envia = forms.DateField(label="Fecha de envio",widget=forms.SelectDateWidget(attrs={'type': 'date','class':'form-control'}), required=True)
    Email = forms.EmailField(label="Email", required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    Camp = forms.ChoiceField(choices=CAMPOS,widget=forms.Select(attrs={'class':'form-control'}))
    Prioridad = forms.CharField(label="Prioridad",widget=forms.TextInput(attrs={'class':'form-control'}))
