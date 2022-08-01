from django.urls import path
from . import views

urlpatterns = [
    path('', views.FormView.formu_index, name="formulario"),
    path('campanha/campanha_enviada/', views.FormView.formu_index, name="campaña"),
]