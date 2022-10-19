from django.apps import AppConfig

#%% Admin Campañas
class FormConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Form'
#%% Admin Proviciones
class QueryformConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'QueryForm'

