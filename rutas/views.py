from django.shortcuts import render
from django.http import HttpResponse
from .models import Entregas
from django.db import connection

def index(request):
    #Primero ejecutamos nuestro stored procedure
    with connection.cursor() as cursor:
        cursor.callproc('obtener_entregas_pendientes')
        resultados = cursor.fetchall()
    
    entregas_pendientes = []
    for fila in resultados:
        entrega = {}
        entrega['cliente'] = fila[0]
        entrega['tipo_entrega'] = fila[1]
        entregas_pendientes.append(entrega)
    
    return render(request, 'index.html' , {'entregas_pendientes': entregas_pendientes})

def entregasTerminadas(request):
    return render(request , 'entregasTerminadas.html')

#Aqui vamos a poder agregar una ruta y cliente
def rutasPorHacer(request):
    #Para obtener los repartidores
    with connection.cursor() as cursor:
        cursor.callproc('obtener_repartidores_libres')
        resultados = cursor.fetchall()

    # Convertir a lista de diccionarios
    repartidores_libres = []
    for fila in resultados:
        repartidores_libres.append({
            'id': fila[0],
            'nombre': fila[1],
            'telefono': fila[2],
        })

    #Para obtener la información
    if request.method == 'POST':
        accion = request.POST.get('accion')

        # Campos comunes
        nombre = request.POST.get('nombre_cliente')
        telefono = request.POST.get('telefono')
        calle = request.POST.get('calle')
        num_int = request.POST.get('num_int')
        num_ext = request.POST.get('num_ext')
        colonia = request.POST.get('colonia')
        municipio = request.POST.get('municipio')
        cp = request.POST.get('cp')
        tipo_entrega = request.POST.get('tipo_entrega')
        beneficio = request.POST.get('beneficio')
        monto = request.POST.get('monto')

        if accion == 'agregar':
            print('agregamos clientes')
        elif accion == 'generar':
            repartidores = request.POST.getlist('repartidores')
            print("Generando ruta con repartidores:", repartidores)

    return render(request, 'rutasPorHacer.html' , {'repartidores_libres': repartidores_libres})
