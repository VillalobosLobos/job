#Aquí pondre operacoines relacionadas a las rutas
from app.forms import Crear_cliente, Crear_direccion, Crear_entrega
from app.views.entregas.entregas_crud import crear_entrega
from django.shortcuts import render, redirect
from django.contrib import messages
from app.models import Entregas

def rutas_por_hacer(request):
    if request.method == 'GET':
        entregas_reagendadas = Entregas.objects.filter(estado_de_la_entrega="reagendada")

        return render(request, 'rutas/crear_form.html', {
        'formulario_cliente': Crear_cliente,
        'formulario_direccion': Crear_direccion,
        'formulario_entrega': Crear_entrega,
        'reagendada' : entregas_reagendadas
    })
    else:
        entrega = crear_entrega(request.POST)
        if entrega is None:
            messages.error(request, 'Hubo un problema al crear la entrega. Intenta nuevamente.')
        else:
            messages.success(request, 'Entrega creada exitosamente.')
        return redirect('/rutas_por_hacer/')