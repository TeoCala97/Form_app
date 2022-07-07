from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePage(TemplateView):
    template_name: "core/base.html"

    def WelcomePage(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Campañas Sodimac"
        return context 