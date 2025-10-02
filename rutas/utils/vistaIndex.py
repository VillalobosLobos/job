from django.db import connection

def obtener_entregas_pendientes():
    #Primero ejecutamos nuestro stored procedure
    with connection.cursor() as cursor:
        cursor.callproc('seleccionar_entregas_pendientes')
        resultados = cursor.fetchall()
    
    entregas_reagendadas = []
    for fila in resultados:
        entrega = {}
        entrega['cliente'] = fila[0]
        entrega['tipo_entrega'] = fila[1]
        entregas_reagendadas.append(entrega)
    return entregas_reagendadas