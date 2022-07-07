from django.urls import path
from . import views
from .views import HomePage

urlpatterns = [
    path('Campañas_enviadas/', HomePage.as_view(), name="sample"),
]