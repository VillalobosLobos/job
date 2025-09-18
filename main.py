import utils.vehiculo as transporte
import utils.info as csv
import utils.grafo as g
import utils.ruta as rut
import osmnx as ox
import os

os.system("clear")

#Todo esto para obtener los puntos de inicio, fin y entrega de un CSV
cont = csv.obtenerCSV("data/bd.csv") #Contenido del CSV
puntos = csv.obtenerFinInicio(cont) #Regresa punto de inicio y fin de la ruta
inicio = csv.direcciones(puntos[0]) # Dirección del inicio
fin = csv.direcciones(puntos[1]) # Dirección del fin
puntosEntrega = csv.obtenerPuntos(cont) # Puntos de entrega(sin incluir fin e inicio)

#Para tener los modelos de motos y autos para realizar la entrega
contTransporte = transporte.obtenerContenido("confVehiculo.json")
modMotos = transporte.obtenerMotos(contTransporte)
modAutos = transporte.obtenerAutos(contTransporte)

#Para obtener el grafo
#g.generarGrafoCDMX()
grafo = g.obtenerGrafo()

'''
print(f'Inicio de la ruta:\n{inicio}\n\nFin de la ruta:\n{fin} \nPuntos a recorrer: {puntosEntrega}\n')

print(f'\nEn que vehículo iniciara el recorrido?\n',end='')
print(modMotos)
print(modAutos)
transporte.modificarStatus("confVehiculo.json", "A", "A001")
'''
nuevo = rut.crearNodosPuntos(grafo, cont)
grafoProyectado = ox.project_graph(grafo)
matriz = rut.crearMatrizDistancias(grafoProyectado, nuevo)
ruta_optima = rut.resolverTSP(matriz)
print("Orden óptimo de entrega:", ruta_optima)

#print(cont[['nombreCliente', 'nodo']])

#grafo = ox.load_graphml(filepath='data/zonaMetropolitana.graphml')
#ox.plot_graph(grafo)

