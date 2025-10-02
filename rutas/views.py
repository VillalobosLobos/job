from django.shortcuts import render
from .utils import vistaRutasPorHacer as vrph
from .utils import vistaIndex as vi
from .utils import vistaEntregasTerminadas as vet
from .forms import RutaForm
from django.shortcuts import get_object_or_404, redirect
from .models import Entregas

def index(request):
    entregas_pendientes = vi.obtener_entregas_pendientes()
    
    return render(request, 'index.html' , {'entregas_pendientes': entregas_pendientes})

def entregasTerminadas(request):
    entregas_terminadas = vet.obtener_entregas_terminadas()
    return render(request , 'entregasTerminadas.html', {'entregas_terminadas':entregas_terminadas})

#Aqui vamos a poder agregar una ruta y cliente
def rutasPorHacer(request):
    entregas_reagendadas = vrph.obtener_entregas_reagendadas()
    repartidores_libres = vrph.obtener_repartidores_libres()
    entrega_a_editar = None

    if request.method == 'POST':
        if 'editar_id' in request.POST:
            # Cargar datos para edición
            entrega_id = request.POST['editar_id']
            entrega_a_editar = Entregas.objects.get(id_entrega=entrega_id)
            form = RutaForm(instance=entrega_a_editar)
        else:
            # Guardar datos nuevos o modificados
            form = RutaForm(request.POST)
            if form.is_valid():
                datos = form.cleaned_data
                if 'id_entrega' in request.POST:
                    entrega = Entregas.objects.get(id_entrega=request.POST['id_entrega'])
                    for campo, valor in datos.items():
                        setattr(entrega, campo, valor)
                    entrega.save()
                else:
                    Entregas.objects.create(**datos)
                form = RutaForm()
    else:
        form = RutaForm()

    return render(request, 'rutasPorHacer.html', {
        'form': form,
        'entregas_reagendadas': entregas_reagendadas,
        'repartidores_libres': repartidores_libres,
        'entrega_a_editar': entrega_a_editar
    })


def eliminarEntrega(request, id_entrega):
    entrega = get_object_or_404(Entregas, id_entrega=id_entrega)
    if request.method == 'POST':
        entrega.delete()
    return redirect('rutas')
