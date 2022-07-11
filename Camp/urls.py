from django.urls import path
from .views import CampView

urlpatterns = [
    path('campanha_enviada/', CampView.as_view() , name="campaña"),
]