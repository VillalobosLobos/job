from django.db import connection

def obtener_entregas_reagendadas():
    with connection.cursor() as cursor:
        cursor.callproc('seleccionar_entregas_reagendadas')
        resultados = cursor.fetchall()
    
    entregas_reagendadas = []
    for fila in resultados:
        entrega = {}
        entrega['id_entrega'] = fila[0]
        entrega['cliente'] = fila[1]
        entrega['tipo_entrega'] = fila[2]
        entregas_reagendadas.append(entrega)
    return entregas_reagendadas


def obtener_repartidores_libres():
    #Primero ejecutamos nuestro stored procedure
    with connection.cursor() as cursor:
        cursor.callproc('seleccionar_repartidores_libres')
        resultados = cursor.fetchall()
    
    repartidores_libres = []
    for fila in resultados:
        repartidores_libres.append({
            'id': fila[0],
            'nombre': fila[1],
            'telefono': fila[2],
        })
    return repartidores_libres

'''
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
'''