from django.db import models

# Create your models here.
class Camp(models.Model):
    Campanaha_id = models.CharField(max_length=20)
    Nombre_campanha = models.CharField(max_length=20)
    N_registro = models.IntegerField(verbose_name="Numero de registro")
    Created = models.DateTimeField(auto_now_add=True ,verbose_name="fecha de creación")
    Updated = models.DateTimeField(auto_now=True ,verbose_name="fecha de edición")

    class Meta:
        verbose_name = "Camp"
        verbose_name_plural = "Camps"
        ordering = ["-Created"]

    def __str__(self):
        return self.Nombre_campanha