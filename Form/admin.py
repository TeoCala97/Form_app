from django.contrib import admin
from .models import Query, forms_api

#%% Admin Campañas
class FormAdmin(admin.ModelAdmin):
    list_display = ('Nombre_campanha', 'Marca', 'Canal', 'Fecha_envio', 'Tipo_usuario', 'Prioridad','Segmento_necesidad')

admin.site.register(forms_api, FormAdmin)
#%% Admin Proviciones
# class QueryAdmin(admin.ModelAdmin):
#     list_display = ('qname','select','fecha')

# admin.site.register(Query, FormAdmin)