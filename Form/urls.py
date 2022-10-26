from django.urls import path
from .views import FormView,QueryView,CampView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('formularios/campanha/', login_required(FormView.as_view()), name="formulario"),
    path('formularios/reportes/', login_required(CampView.as_view()), name="resporte"),
    path('formularios/provisiones/', login_required(QueryView.as_view()), name="provisiones"),
]