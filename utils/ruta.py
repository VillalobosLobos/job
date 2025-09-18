from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import pandas as pd
import osmnx as ox
import networkx as nx
import numpy as np

def crearMatrizDistancias(grafo, df_clientes):
    """
    Crea la matriz de distancias entre todos los clientes usando su nodo OSMnx.
    
    Parámetros:
        grafo : networkx.MultiDiGraph
            Grafo proyectado de OSMnx.
        df_clientes : pd.DataFrame
            DataFrame con columna 'nodo' para cada cliente.
    
    Retorna:
        np.array : matriz n x n de distancias en metros
    """
    n = len(df_clientes)
    dist_matrix = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            if i != j:
                try:
                    # Distancia más corta en metros
                    dist_matrix[i][j] = nx.shortest_path_length(
                        grafo,
                        df_clientes.loc[i, 'nodo'],
                        df_clientes.loc[j, 'nodo'],
                        weight='length'
                    )
                except nx.NetworkXNoPath:
                    # Penalizar si no hay camino
                    dist_matrix[i][j] = 999999
            else:
                dist_matrix[i][j] = 0  # distancia de un punto a sí mismo
    
    return dist_matrix

def resolverTSP(dist_matrix):
    """
    Resuelve el TSP y devuelve el orden óptimo de visitas.
    
    Parámetros:
        dist_matrix : np.array
            Matriz n x n de distancias entre clientes.
    
    Retorna:
        list : índice de clientes en el orden óptimo.
    """
    n = len(dist_matrix)
    
    # Crear manager y modelo de routing
    manager = pywrapcp.RoutingIndexManager(n, 1, 0)  # 1 vehículo, inicia en nodo 0
    routing = pywrapcp.RoutingModel(manager)
    
    # Función de costo de viaje (distancia)
    def distancia_callback(from_index, to_index):
        return int(dist_matrix[manager.IndexToNode(from_index)][manager.IndexToNode(to_index)])
    
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
    
	# Lista para almacenar nodos más cercanos
	nodos = []
    
	# Recorrer cada fila del DataFrame
	for index, fila in cont.iterrows():
		latitud = fila['latitud']
		longitud = fila['longitud']
        
		# Buscar nodo más cercano en el grafo proyectado
		nodoCercano = ox.distance.nearest_nodes(grafoProyectado, X=longitud, Y=latitud)
		nodos.append(nodoCercano)
    
	# Agregar columna 'nodo' al DataFrame
	cont['nodo'] = nodos
    
	return cont


