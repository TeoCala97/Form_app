from django.urls import path
from .views import TableCampView, TableProvView, TableRepoView


urlpatterns = [
    path('tablas/campanha', TableCampView.as_view(), name="tablacamp"),
    path('tablas/provisiones', TableProvView.as_view(), name="tablaprov"),
    path('tablas/reportes', TableRepoView.as_view(), name="tablarep"),
]