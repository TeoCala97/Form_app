from django.contrib import admin
from .models import forms_api
# Register your models here.
class FormAdmin(admin.ModelAdmin):
    list_display = ('Nombre_campanha', 'Marca', 'Canal', 'Fecha_envio', 'Tipo_usuario', 'Prioridad')

admin.site.register(forms_api, FormAdmin)