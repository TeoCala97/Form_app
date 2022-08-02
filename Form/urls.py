from django.urls import path
from .views import FormView,MenuView

urlpatterns = [
    path('menu/', MenuView.as_view(), name="menu"),
    path('campanha/', FormView.as_view(), name="formulario"),
    path('campanha/campanha_enviada/', FormView.as_view(), name="campaña"),
]