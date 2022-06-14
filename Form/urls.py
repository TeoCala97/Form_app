from django.urls import path
from . import views

urlpatterns = [
    path('', views.formu, name="formulario"),
    path('?ok', views.formu, name="Json"),
]