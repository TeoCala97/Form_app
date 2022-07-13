import imp
from django.db import models
from django.db.models import JSONField

# Create your models here.
class Camp(models.Model):
    data = JSONField()
    def __str__(self):
        return self.Nombre_campanha