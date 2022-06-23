from django.contrib import admin
from Camp.models import Camp

# Register your models here.
class CampAdmin(admin.ModelAdmin):
    # readonly_fields = ('Created') 
    list_display = ('Campanaha_id', 'Nombre_campanha','N_registro')
admin.site.register(Camp, CampAdmin)