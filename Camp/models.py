import imp
from django.db import models
from django.db.models import JSONField
from django.core.serializers.json import DjangoJSONEncoder
import json
# Create your models here.

class Camp(models.Model):
    data = JSONField(null=True, blank=True)

    def __str__(self):
        return self.data