from ssl import create_default_context
from typing import DefaultDict
from django.db import models
from pyparsing import nullDebugAction
from datetime import datetime as time
from multiselectfield import MultiSelectField

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
        ("",""),
        ("ONLINE", "ONLINE"),
        ("HARD", "HARD"),
        ("SOFT", "SOFT"),
        ("TODOS", "TODOS"),
        ("ACABADOS", "ACABADOS"),
        ("MIX", "MIX"),
    ]
    SEGMENTO_NECESIDAD = [
        ("CONSTRUCTOR DE JARDINES", "CONSTRUCTOR DE JARDINES"),
        ("TBD", "TBD"),
        ("VENTA EMPRESA", "VENTA EMPRESA"),
        ("TODERO", "TODERO"),
        ("PINTOR", "PINTOR"),
        ("ELECTRICISTA", "ELECTRICISTA"),
        ("ORNAMENTADOR", "ORNAMENTADOR"),
        ("MULTIESPECIALIDAD CONTRATISTA", "MULTIESPECIALIDAD CONTRATISTA"),
        ("HOGAR", "HOGAR"),
        ("MAESTRO", "MAESTRO"),
        ("ESPECIALISTA ACABADOS", "ESPECIALISTA ACABADOS"),
        ("CARPINTERO", "CARPINTERO"),
        ("PLOMERO", "PLOMERO"),
        ("NO CONTRUCTOR", "NO CONTRUCTOR"),
        ("DECORADOR", "DECORADOR"),
        ("ESPECIALISTA DRYWALL", "ESPECIALISTA DRYWALL"),
    ]   
    SEGMENTO_VALOR = [
        ("",""),
        ("S","S"),
        ("REGULAR","REGULAR"),
        ("VENTA EMPRESA","VENTA EMPRESA"),
    ]  
    CICLO_VIDA = [
        ("DESARROLLO","DESARROLLO"),
        ("MADURO","MADURO"),
        ("VENTA EMPRESA","VENTA EMPRESA"),
        ("POTENCIAL","POTENCIAL"),
        ("REACTIVADO","REACTIVADO"),
        ("FUGADO","FUGADO"),
        ("ADQUISICION","ADQUISICION"),
        ("VENTA","VENTA"),
        ("RETENCION","RETENCION"),
        ("NUEVO","NUEVO"),
        ("RECUPERACION","RECUPERACION"),
    ]  
    TIENDA_FRECUENTE = [
        ("Dorado","DORADO"),
        ("Avda. 68 Sur Bogota","AVDA. 68 SUR BOGOTA"),
        ("Medellin San Juan","MEDELLIN SAN JUAN"),
        ("Envigado","ENVIGADO"),
        ("Medellin Molinos","MEDELLIN MOLINOS"),
        ("Cali Norte","CALI NORTE"),
        ("AVDA. 68 SUR BOGOTA","AVDA. 68 SUR BOGOTA"),
        ("RIONEGRO","RIONEGRO"),
        ("SUBA","SUBA"),
        ("NORTE BOGOTA","NORTE BOGOTA"),
        ("CALI NORTE","CALI NORTE"),
        ("CARTAGENA LA POPA","CARTAGENA LA POPA"),
        ("Cali Sur","CALI SUR"),
        ("Bello","BELLO"),
        ("Palmira Unicentro","PALMIRA UNICENTRO"),
        ("Yopal","YOPAL"),
        ("Dorado Bogota","DORADO BOGOTA"),
        ("MOSQUERA","MOSQUERA"),
        ("CALIMA BOGOTA","CALIMA BOGOTA"),
        ("CUCUTA","CUCUTA"),
        ("ARMENIA","ARMENIA"),
        ("Cajica","CAJICA"),
        ("TULUA EL RETIRO","TULUA EL RETIRO"),
        ("Ibague","IBAGUE"),
        ("Girardot","GIRARDOT"),
        ("Bucaramanga La Rosita","BUCARAMANGA LA ROSITA"),
        ("TINTAL","TINTAL"),
        ("CALI SUR","CALI SUR"),
        ("CARTAGENA SAN FERNANDO","CARTAGENA SAN FERNANDO"),
        ("Mzls San Rafael","MANIZALES SAN RAFAEL"),
        ("Neiva San Pedro","NEIVA SAN PEDRO"),
        ("Valledupar Guatapuri","VALLEDUPAR GUATAPURI"),
        ("SOACHA","SOACHA"),
        ("BARRANQUILLA CENTRO","BARRANQUILLA CENTRO"),
        ("Cedritos Bogota","CEDRITOS BOGOTA"),
        ("Calima Bogota","CALIMA BOGOTA"),
        ("OAT","OAT"),
        ("VCIO FUNDADORES","VILLAVICENCIO FUNDADORES"),
        ("VENTA DISTANCIA BOGOTA","VENTA DISTANCIA BOGOTA"),
        ("Calle 80 Bogota","CALLE 80 BOGOTA"),
        ("Pereira","PEREIRA"),
        ("HOMECENTER MALLPLAZA NQS","HOMCENTER MALLPLAZA NQS"),
        ("MONTERIA EL RECREO","MONTERIA EL RECREO"),
        ("BARRANQUILLA NORTE","BARRANQUILLA NORTE"),
        ("Medellin Insdustriales","MEDELLIN INDUSTRIALES"),
        ("Centro de Distribucion (900)","CENTRO DE DISTRIBUCION (900)"),
        ("Barranquilla Calle 30","BARRANQUILLA CALLE 3O"),
        ("TUNJA","TUNJA"),
        ("SANTA MARTA BUENAVISTA","SANTA MARTA BUENAVISTA"),
    ]  

    Id = models.AutoField(primary_key=True)
    Nombre_campanha = models.CharField(max_length=200, verbose_name="Nombre Campaña")
    Marca =  models.CharField(max_length=10,choices=MARCAS,verbose_name="Marca")
    Canal =  models.CharField(max_length=10,choices=CANAL,verbose_name="Canal")
    Fecha_envio = models.DateField()
    Email = models.EmailField()
    Tipo_usuario =  models.CharField(max_length=10,choices=TIPO,verbose_name="Tipo de Usuario", default=None, blank=True, null=True)
    Table_name = models.CharField(max_length=200,verbose_name="Nombre de Tabla", default=None, blank=True, null=True)
    Nombre_campo = models.CharField(max_length=100, default=None,verbose_name="Nombre del Campo", null=True, blank=True)
    Valor_Campo = models.CharField(max_length=100, default=None,verbose_name="Valor del Campo", blank=True, null=True)
    Prioridad = models.CharField(max_length=10,verbose_name="Prioridad")
    Segmento_necesidad =  MultiSelectField(choices=SEGMENTO_NECESIDAD, blank=True, null=True) #multiple
    Segmento_valor =  models.CharField(max_length=20,choices=SEGMENTO_VALOR,verbose_name="Segmento Valor", blank=True, null=True)
    Ciclo_vida =  MultiSelectField(choices=CICLO_VIDA, blank=True, null=True) # multiple
    Tienda_frecuente =  models.CharField(max_length=30,choices=TIENDA_FRECUENTE,verbose_name="Tienda Frecuente", blank=True, null=True)
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
