from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def landing(request):
    return render(request, "template.html")