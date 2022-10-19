from ssl import create_default_context
from typing import DefaultDict
from django.db import models
from pyparsing import nullDebugAction
from datetime import datetime as time

#%% Admin Campañas
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
    
    Nombre_campanha = models.CharField(max_length=200, verbose_name="Nombre Campaña")
    Marca =  models.CharField(max_length=10,choices=MARCAS,verbose_name="Marca")
    Canal =  models.CharField(max_length=10,choices=CANAL,verbose_name="Canal")
    Fecha_envio = models.DateField()
    Email = models.EmailField()
    Tipo_usuario =  models.CharField(max_length=10,choices=TIPO,verbose_name="Segmento Necesidad", default=None)
    Table_name = models.CharField(max_length=200,verbose_name="Segmento Valor", default=None, blank=True, null=True)
    Nombre_campo = models.CharField(max_length=100, default=None,verbose_name="Ciclo de Vida", null=True, blank=True,)
    Valor_Campo = models.CharField(max_length=100, default=None,verbose_name="Tienda Frecuente", blank=True, null=True)
    Prioridad = models.CharField(max_length=10,verbose_name="Prioridad")
    Created = models.DateTimeField(auto_now_add=True ,verbose_name="fecha de creación")
    Updated = models.DateTimeField(auto_now=True ,verbose_name="fecha de edición")
    class Meta:
        verbose_name = "form_api"
        verbose_name_plural = "form_apis"
        ordering = ["-Created"]

    def __str__(self):
        return self.Nombre_campanha

#%% Admin Provisiones
class Query(models.Model):

    LISTA = [("",""),
            ("S1","Seleccion 1"),
            ("S2","Seleccion 2"),
            ("S3","Seleccion 3"),
            ("S4","Seleccion 4"),
            ("S5","Seleccion 5"),]

    qname = models.CharField(max_length=200, verbose_name="Nombre")
    select =  models.CharField(max_length=10,choices=LISTA,verbose_name="Desplegables")
    fecha = models.DateField()
    created = models.DateTimeField(auto_now_add=True ,verbose_name="fecha de creación")
    updated = models.DateTimeField(auto_now=True ,verbose_name="fecha de edición")

    class Meta:
        verbose_name = "Query"
        verbose_name_plural = "Query"
        ordering = ["-created"]
    
    def __str__(self):
        return self.qname
