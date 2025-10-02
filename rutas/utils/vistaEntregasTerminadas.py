from django.db import connection

def obtener_entregas_terminadas():
    #Primero ejecutamos nuestro stored procedure
    with connection.cursor() as cursor:
        cursor.callproc('seleccionar_entregas_terminadas')
        resultados = cursor.fetchall()
    
    entregas_terminadas = []
    for fila in resultados:
        entrega = {}
        entrega['cliente'] = fila[0]
        entrega['tipo_entrega'] = fila[1]
        entregas_terminadas.append(entrega)
    return entregas_terminadas