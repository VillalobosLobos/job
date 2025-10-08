from app.models import Repartidores, Vehiculos, Clientes, Direcciones, Entregas
from app.forms import Crear_cliente, Crear_direccion, Crear_entrega
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
import logging

logger = logging.getLogger(__name__)

def crear_entrega(data):
    try:
        with transaction.atomic():
            repartidor = Repartidores.objects.get(id=1)
            vehiculo = Vehiculos.objects.get(id=1)

            cliente = Clientes.objects.create(
                nombre = data['nombre'],
                telefono = data['telefono']
            )

            direccion = Direcciones.objects.create(
                id_cliente = cliente,
                calle = data['calle'],
                numero_exterior = data['numero_exterior'],
                numero_interior = data['numero_interior'],
                colonia = data['colonia'],
                delegacion = data['delegacion'],
                cp = data['cp']
            )

            entrega = Entregas.objects.create(
                id_cliente = cliente,
                id_direccion = direccion,
                #id_repartidor = repartidor,
                #id_vehiculo = vehiculo,
                tipo_de_entrega = data['tipo_de_entrega'],
                beneficios = data['beneficios'],
                monto = data['monto']
            )

            return entrega  # éxito

    except Exception as e:
        logger.error(f"Error al crear entrega: {e}")
        return None

def editar_entrega(request, id):
    entrega = Entregas.objects.get(id=id)
    cliente = entrega.id_cliente
    direccion = entrega.id_direccion

    form_cliente = Crear_cliente(initial={
        'nombre': cliente.nombre,
        'telefono': cliente.telefono
    })

    form_direccion = Crear_direccion(initial={
        'calle': direccion.calle,
        'numero_exterior': direccion.numero_exterior,
        'numero_interior': direccion.numero_interior,
        'colonia': direccion.colonia,
        'delegacion': direccion.delegacion,
        'cp': direccion.cp
    })

    form_entrega = Crear_entrega(initial={
        'tipo_de_entrega': entrega.tipo_de_entrega,
        'beneficios': entrega.beneficios,
        'monto': entrega.monto
    })

    return render(request, 'rutas/crear_form.html', {
        'formulario_cliente': form_cliente,
        'formulario_direccion': form_direccion,
        'formulario_entrega': form_entrega,
        'reagendada': Entregas.objects.filter(estado_de_la_entrega="reagendada")
    })

def eliminar_entrega(request, id_entrega):
    entrega = get_object_or_404(Entregas, id=id_entrega)
    if request.method == "POST":
        cliente = entrega.id_cliente
        direccion = entrega.id_direccion
        entrega.delete()
        cliente.delete()
        direccion.delete()
        
    return redirect('/rutas_por_hacer/')

