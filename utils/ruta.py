from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import networkx as nx
import pandas as pd
import osmnx as ox
import numpy as np
import pyproj

def calcularDistanciaTotal(grafoProyectado, rutaNodos):
    """
    Calcula la distancia total de una ruta sobre el grafo proyectado.

    Parámetros:
        grafoProyectado : networkx.MultiDiGraph
            Grafo con información de aristas y longitudes.
        rutaNodos : list
            Lista completa de nodos que conforman la ruta.

    Retorna:
        float : distancia total recorrida en kilómetros
    """
    distanciaTotalMetros = 0

    for i in range(len(rutaNodos)-1):
        u = rutaNodos[i]
        v = rutaNodos[i+1]

        # Cada arista puede ser un MultiDiGraph (varias aristas entre u-v)
        data = grafoProyectado.get_edge_data(u, v)
        if data is not None:
            # Tomamos la primera arista disponible
            length = list(data.values())[0]['length']
            distanciaTotalMetros += length

    distanciaTotalKM = distanciaTotalMetros / 1000
    return distanciaTotalKM


def convertirRutaACoords(grafoProyectado, rutaNodos):
    """
    Convierte una lista de nodos del grafo proyectado a coordenadas WGS84 (lat, lon).
    
    Parámetros:
        grafoProyectado : networkx.MultiDiGraph
            Grafo proyectado con nodos x,y.
        rutaNodos : list
            Lista de nodos que representan la ruta completa.
    
    Retorna:
        list : lista de tuplas (lat, lon)
        transformador : objeto pyproj.Transformer para futuras conversiones
    """
    crsGrafo = grafoProyectado.graph['crs']
    transformador = pyproj.Transformer.from_crs(crsGrafo, "EPSG:4326", always_xy=True)
    
    rutaCoords = [
        transformador.transform(grafoProyectado.nodes[n]['x'], grafoProyectado.nodes[n]['y'])[::-1]
        for n in rutaNodos
    ]
    
    return rutaCoords, transformador


def rutaCompletaNodos(rutaOptima, grafoProyectado, nuevo):
    rutaNodos = []

    for i in range(len(rutaOptima)-1):
        nodoInicio = nuevo.loc[rutaOptima[i], 'nodo']
        nodoFin = nuevo.loc[rutaOptima[i+1], 'nodo']

        # Obtener camino más corto entre nodos en grafo proyectado
        camino = nx.shortest_path(grafoProyectado, nodoInicio, nodoFin, weight='length')

        # Evitar repetir el nodo inicial al concatenar caminos
        if i > 0:
            camino = camino[1:]

        rutaNodos.extend(camino)

    # ------------------------------
    # Obtener coordenadas lat/lon de la ruta
    # ------------------------------
    rutaCoords = [(grafoProyectado.nodes[n]['y'], grafoProyectado.nodes[n]['x']) for n in rutaNodos]

    return rutaCoords, rutaNodos

def crearMatrizDistancias(grafo, dfClientes):
    """
    Crea la matriz de distancias entre todos los clientes usando su nodo OSMnx.
    
    Parámetros:
        grafo : networkx.MultiDiGraph
            Grafo proyectado de OSMnx.
        dfClientes : pd.DataFrame
            DataFrame con columna 'nodo' para cada cliente.
    
    Retorna:
        np.array : matriz n x n de distancias en metros
    """
    n = len(dfClientes)
    distMatrix = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            if i != j:
                try:
                    # Distancia más corta en metros
                    distMatrix[i][j] = nx.shortest_path_length(
                        grafo,
                        dfClientes.loc[i, 'nodo'],
                        dfClientes.loc[j, 'nodo'],
                        weight='length'
                    )
                except nx.NetworkXNoPath:
                    # Penalizar si no hay camino
                    distMatrix[i][j] = 999999
            else:
                distMatrix[i][j] = 0  # distancia de un punto a sí mismo
    
    return distMatrix

def resolverTSP(distMatrix):
    """
    Resuelve el TSP y devuelve el orden óptimo de visitas.
    
    Parámetros:
        distMatrix : np.array
            Matriz n x n de distancias entre clientes.
    
    Retorna:
        list : índice de clientes en el orden óptimo.
    """
    n = len(distMatrix)
    
    # Crear manager y modelo de routing
    manager = pywrapcp.RoutingIndexManager(n, 1, 0)  # 1 vehículo, inicia en nodo 0
    routing = pywrapcp.RoutingModel(manager)
    
    # Función de costo de viaje (distancia)
    def distancia_callback(from_index, to_index):
        return int(distMatrix[manager.IndexToNode(from_index)][manager.IndexToNode(to_index)])
    
    transit_callback_index = routing.RegisterTransitCallback(distancia_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    
    # Estrategia de búsqueda
    search_params = pywrapcp.DefaultRoutingSearchParameters()
    search_params.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    search_params.local_search_metaheuristic = routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
    search_params.time_limit.seconds = 10  # Ajustable
    
    # Resolver
    solution = routing.SolveWithParameters(search_params)
    
    if solution:
        ruta = []
        index = routing.Start(0)
        while not routing.IsEnd(index):
            ruta.append(manager.IndexToNode(index))
            index = solution.Value(routing.NextVar(index))
        ruta.append(manager.IndexToNode(index))  # volver al inicio
        return ruta
    else:
        return None

def crearNodosPuntos(grafo, cont):
	grafoProyectado = ox.project_graph(grafo)

	crs_grafo = grafoProyectado.graph['crs']
	transformador = pyproj.Transformer.from_crs("EPSG:4326", crs_grafo, always_xy=True)

	# Lista para almacenar nodos más cercanos
	nodos = []
    
	# Recorrer cada fila del DataFrame
	for index, fila in cont.iterrows():
		latitud = fila['latitud']
		longitud = fila['longitud']
        
		x, y = transformador.transform(longitud, latitud)

		# Buscar nodo más cercano en el grafo proyectado
		nodoCercano = ox.distance.nearest_nodes(grafoProyectado, X=x, Y=y)
		nodos.append(nodoCercano)
    
	# Agregar columna 'nodo' al DataFrame
	cont['nodo'] = nodos
    
	return cont


