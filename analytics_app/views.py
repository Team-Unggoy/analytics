from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'analytics_app/login.html'

    


def landing(request):
    return render(request, "template.html")