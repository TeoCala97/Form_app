from django.urls import path
from .views import FormView

urlpatterns = [
    path('campanha/', FormView.as_view(), name="formulario"),
    path('campanha/campanha_enviada/', FormView.as_view(), name="campaña"),
]