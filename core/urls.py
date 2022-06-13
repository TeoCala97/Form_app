from django.urls import path
from . import views

urlpatterns = [
    path('Campañas_enviadas/', views.sample, name="sample"),
]