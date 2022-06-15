from django.db import models
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
            
    
    Nombre_campania = models.CharField(max_length=200)
    Marca =  models.CharField(max_length=10,choices=MARCAS)
    Canal =  models.CharField(max_length=10,choices=CANAL)
    Fecha_envia = models.DateField()
    Email = models.EmailField()
    Camp =  models.CharField(max_length=10,choices=CAMPOS)
    Prioridad = models.CharField(max_length=10)
    
    def __str__(self):
        return self.Nombre_campania
