from django.urls import path
from . import views

urlpatterns = [
    path('Campaign/', views.formu, name="formulario"),
    path('?ok', views.formu, name="Json"),
]