from django.urls import path
from . import views

urlpatterns = [
    path('campanha/campanha_enviada/', views.CampView.Camp_get, name="campaña"),
]