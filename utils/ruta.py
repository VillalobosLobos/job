from networkx.algorithms import approximation
from utils.verRuta import rutaFinal
import networkx as nx
import osmnx as ox

def TSP(grafoNuevo, nodosVisitas):
    # Resuelve el TSP usando el grafo de nuevo
    rutaOptima = approximation.traveling_salesman_problem(grafoNuevo, nodes=nodosVisitas)
    return rutaOptima

def crearNuevoGrafo(distancias):
    grafoNuevo = nx.DiGraph() #Grafo dirigido
    for (val1, val2), distancia in distancias.items():
        grafoNuevo.add_edge(val1, val2, weight=distancia)
    
    print("Grafo creado")
    return grafoNuevo
    #TSP(grafoNuevo, nodosVisitas)

def distanciasVisitas(nodosVisitas, grafo):
    distancias = {}

    for val1 in nodosVisitas:
        for val2 in nodosVisitas:
            if val1 != val2: # Para evitar la distancia del nodo a sí mismo
                # Consideramos tiempo de viaje
                distancia = nx.shortest_path_length(grafo, source=val1, target=val2, weight='travel_time')
                distancias[(val1, val2)] = distancia
    
    print("Distancias obtenidas")
    return distancias
    #crearNuevoGrafo(distancias, nodosVisitas)

def ruta(puntoInicio, puntosVisitas, grafo):
    visitas = puntosVisitas + [ puntoInicio ]

    #Calculamos velocidad
    grafo = ox.add_edge_speeds(grafo)
    #Calculamos distancia
    grafo = ox.add_edge_travel_times(grafo)

    nodosVisitas = []
    for latitud, longitud in visitas:
        #Obtenemos el nodo más cercano a la ubicación
        nodoMasCercano = ox.distance.nearest_nodes(grafo, longitud, latitud)
        nodosVisitas.append(nodoMasCercano)
    
    distancias = distanciasVisitas(nodosVisitas, grafo)
    grafoNuevo = crearNuevoGrafo(distancias)
    rutaOptima = TSP(grafoNuevo, nodosVisitas)

    m = rutaFinal(rutaOptima, grafo)
    m.save("ruta.html")
