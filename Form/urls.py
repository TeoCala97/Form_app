from django.urls import path
from . import views

urlpatterns = [
    path('campaña/', views.FormView.formu_index, name="formulario"),

]