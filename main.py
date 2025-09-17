import utils.vehiculo as transporte
import utils.info as csv
import utils.grafo as g
import osmnx as ox
import os

os.system("clear")

calle = ''
numExt = ''
numInt = ''
colonia = ''
alcalMun = ''
cp = ''

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

#print(f'Inicio de la ruta:\n{inicio}\n\nFin de la ruta:\n{fin} \nPuntos a recorrer: {puntosEntrega}\n')

print(f'Calle : ',end='')
calle = input()
print(f'numExt : ',end='')
numExt = input()
print(f'numInt : ',end='')
numInt = input()
print(f'Colonia : ',end='')
colonia = input()
print(f'alcaldia/municipio : ',end='')
alcalMun = input()
print(f'código postal : ',end='')
cp = input()

uso = f'{calle}, {numExt}, {numInt}, {colonia}, {alcalMun}, {cp}'

csv.coordenadasLL("Canarios 313, Portales, Benito Juárez, 03300, Ciudad de México, México")

'''
print(f'\nEn que vehículo iniciara el recorrido?\n',end='')
print(modMotos)
print(modAutos)
transporte.modificarStatus("confVehiculo.json", "A", "A001")
'''
#g.generarGrafo()

#grafo = ox.load_graphml(filepath='data/zonaMetropolitana.graphml')
#ox.plot_graph(grafo)

