from ssl import create_default_context
from typing import DefaultDict
from django.db import models
from pyparsing import nullDebugAction
from datetime import datetime as time

# Create your models here.
class forms_api(models.Model):
    MARCAS = [
        ("", ""),
        ("HC", "Homecenter"),
        ("CT", "Constructor"),
    ]
    CANAL = [
        ("", ""),
        ("EMAIL", "Email"),
        ("SMS", "SMS"),
    ]
    TIPO = [
        ("None", ""),
        ("ONLINE", "ONLINE"),
        ("HARD", "HARD"),
        ("SOFT", "SOFT"),
        ("TODOS", "TODOS"),
        ("ACABADOS", "ACABADOS"),
        ("MIX", "MIX"),
    ] 
    CAMPOS = [
        ("None", ""),
        ("Si", "Si"),
        ("ONLINE", "ONLINE"),
        ("HARD", "HARD"),
        ("SOFT", "SOFT"),
        ("TODOS", "TODOS"),
        ("ACABADOS", "ACABADOS"),
    ]    
    N_CAMP = [
        ("None", ""),
        ("CANJE", "CANJE"),
        ("CAMP", "CAMP"),
    ]    
    
    Nombre_campanha = models.CharField(max_length=200, verbose_name="Nombre Campaña")
    Marca =  models.CharField(max_length=10,choices=MARCAS,verbose_name="Marca")
    Canal =  models.CharField(max_length=10,choices=CANAL,verbose_name="Canal")
    Categoria = models.CharField(max_length=200, verbose_name="Categoria")
    Fecha_envio = models.DateField()
    Email = models.EmailField()
    Tipo_usuario =  models.CharField(max_length=10,choices=TIPO,verbose_name="Tipo de usuario", default=None)
    Table_name = models.CharField(max_length=200,verbose_name="Nombre de Tabla", default=None, blank=True, null=True)
    Nombre_campo = models.CharField(max_length=100, default=None,verbose_name="Nombre del Campo", null=True, blank=True,)
    Valor_Campo = models.CharField(max_length=100, default=None,verbose_name="Valor del Campo", blank=True, null=True)
    Prioridad = models.CharField(max_length=10,verbose_name="Prioridad")
    Created = models.DateTimeField(auto_now_add=True ,verbose_name="fecha de creación")
    Updated = models.DateTimeField(auto_now=True ,verbose_name="fecha de edición")
    class Meta:
        verbose_name = "form_api"
        verbose_name_plural = "form_apis"
        ordering = ["-Created"]

    def __str__(self):
        return self.Nombre_campanha
