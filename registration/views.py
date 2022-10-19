from tkinter import Widget
from attr import attrs
from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth import login

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView,self).get_form()                    
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'contraseña'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'confirme Contraseña'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'email'})
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'nombre de usuario'})
        return form
