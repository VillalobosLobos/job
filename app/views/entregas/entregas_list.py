#Aquí pondre el listado de las entregas
from django.shortcuts import render
from app.models import Entregas


#Muestra una lista de las entregas pendientes
def estado_de_entrega(request):
    entregas_pendientes = Entregas.objects.filter(estado_de_la_entrega="pendiente")
    return render(request, 'entregas/pendientes_list.html', {'pendientes' : entregas_pendientes})

#Muestra una lista de las entregas terminadas
def entregas_terminadas(request):
    entregas_terminadas = Entregas.objects.filter(estado_de_la_entrega="terminada")
    return render(request, 'entregas/terminadas_list.html', {'terminadas' : entregas_terminadas})





