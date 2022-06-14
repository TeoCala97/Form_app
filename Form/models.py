from django.db import models
# Create your models here.
class forms_api(models.Model):
    Nombre_campania = models.CharField(max_length=200)
    Marca =  models.CharField(max_length=200)
    Canal =  models.CharField(max_length=200)
    Fecha_envia = models.DateField()
    Email = models.EmailField()
    Camp =  models.CharField(max_length=200)
    Prioridad = models.CharField(max_length=10)
    
    def __str__(self):
        return self.Nombre_campania
