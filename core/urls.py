from django.urls import path
from . import views
from .views import HomePage
from registration.views import SignUpView

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
]