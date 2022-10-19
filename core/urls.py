from django.urls import path
from . import views
from .views import HomePage, DashView, LockView, MainView
from registration.views import SignUpView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', HomePage.as_view(), name=""),
    path('dashboard/', login_required(DashView.as_view()), name="dash"),
    path('lock/', login_required(LockView.as_view()), name="lock"),
    path('maintenance/', login_required(MainView.as_view()), name="mainte"),
]