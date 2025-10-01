from django.shortcuts import render
from django.http import HttpResponse
from .models import Entregas

def hola(request):
    total = Entregas.objects.count()
    return HttpResponse(f"Total entregas: {total}")


def index(request):
    return render(request, 'index.html')