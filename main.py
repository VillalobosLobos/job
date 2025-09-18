import utils.vehiculo as transporte
import utils.info as csv
import utils.ruta as rut
import utils.grafo as g
import utils.mapa as m
import networkx as nx
import osmnx as ox
import os

os.system("clear")

print("\nEstos son los vehículos disponibles:")
contenido = transporte.obtenerContenido("confVehiculo.json")
motos = transporte.obtenerMotos(contenido)
autos = transporte.obtenerAutos(contenido)

print(transporte.mostrarVehiculos(motos, autos))

print('Qué vehículo va a utilizar (MId): ', end='')
mId = input()
vehiculo = "autos" if mId[0] == 'A' else "motos"

transporte.cambiarStatusVehiculo("confVehiculo.json", vehiculo, mId[1], "ocupado")

print("\nNombre del repartidor: ", end='')
nombreRepartidor = input()


#Todo esto para obtener los puntos de inicio, fin y entrega de un CSV
cont = csv.obtenerCSV("data/bd.csv") #Contenido del CSV
puntos = csv.obtenerFinInicio(cont) #Regresa punto de inicio y fin de la ruta
inicio = csv.direcciones(puntos[0]) # Dirección del inicio
fin = csv.direcciones(puntos[1]) # Dirección del fin
puntosEntrega = csv.obtenerPuntos(cont) # Puntos de entrega(sin incluir fin e inicio)

#Para obtener el grafo
#g.generarGrafoCDMX()
grafo = g.obtenerGrafo()

#Para obtener la ruta óptima
nuevo = rut.crearNodosPuntos(grafo, cont) #Convierte coordenadas a nodos válidos para el grafo
grafoProyectado = ox.project_graph(grafo)
matriz = rut.crearMatrizDistancias(grafoProyectado, nuevo)
rutaOptima = rut.resolverTSP(matriz)

print(f'nodo nuevo:\n{nuevo}')

rutaCoords, rutaNodos = rut.rutaCompletaNodos(rutaOptima, grafoProyectado, nuevo)
rutaCoords, transformador = rut.convertirRutaACoords(grafoProyectado, rutaNodos)
print(f'Kilometros totales de la ruta: {rut.calcularDistanciaTotal(grafoProyectado, rutaNodos)}')

m.dibujarRutaMapa(nuevo, grafoProyectado, rutaOptima, rutaNodos, transformador)

