from ortools.constraint_solver import pywrapcp, routing_enums_pb2
from sklearn.cluster import KMeans
import networkx as nx
import osmnx as ox
import numpy as np

def generarGrafo():
	zona = "Ciudad de México, México"

	print(f'Descargando el grafo de {zona} ...\n')
	try:
		grafo = ox.graph_from_place(
			zona,
			network_type = "drive",
			simplify = True,
			retain_all = False
		)

		#Guardar el grafo en un archivo .graphml
		ruta = "data/zonaMetropolitana.graphml"
		ox.save_graphml(grafo, filepath = ruta)
		print(f'\nGrafo guardado en {ruta} ...\n')
		#return grafo
	except Exception as e:
		print(f'Ocurrio un error {e} ...')
		return None

def obtenerGrafoProyectado():
	print(f'Obteniendo el grafo proyectado ...')
	grafo = ox.load_graphml("data/zonaMetropolitana.graphml")
	return ox.project_graph(grafo)

def coordenadasANodos(coordenadas, grafo):
	print(f'Obteniendo los nodos cercanos')
	#Mapear las coordenadas a nodos del grafo
	latitudes = [c[0] for c in coordenadas]
	longitudes = [c[1] for c in coordenadas]

	#Para obtener los nodos cerda de las coodenadas
	nodos = ox.distance.nearest_nodes(grafo, X=longitudes, Y=latitudes)

	return nodos

def matrizDistancias(grafo, nodos):
	print(f'Haciendo la matriz de distancia ...')
	n = len(nodos)
	matriz = [[0]*n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			if i == j:
				matriz[i][j] = 0
			else:
				try:
					distancia = nx.shortest_path_length(grafo, nodos[i], nodos[j], weight='length')
					matriz[i][j] = int(round(distancia))
				except (nx.NetworkXNoPath, nx.NodeNotFound):
					matriz[i][j] = 10**7  # penalización si no hay camino
	return matriz

def resolverTSP(matriz):
	print(f'Resolviendo el TSP')
	n = len(matriz)
	manager = pywrapcp.RoutingIndexManager(n, 1, 0)
	routing = pywrapcp.RoutingModel(manager)

	def distancia_callback(from_index, to_index):
		return matriz[manager.IndexToNode(from_index)][manager.IndexToNode(to_index)]

	transit_callback_index = routing.RegisterTransitCallback(distancia_callback)
	routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

	search_parameters = pywrapcp.DefaultRoutingSearchParameters()
	search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

	solution = routing.SolveWithParameters(search_parameters)
	if solution is None:
		return None

	ruta = []
	index = routing.Start(0)
	while not routing.IsEnd(index):
		ruta.append(manager.IndexToNode(index))
		index = solution.Value(routing.NextVar(index))
	ruta.append(manager.IndexToNode(index))
	return ruta

def agruparEntregasIndices(coordenadas, numRepartidores):
    deposito = (0, coordenadas[0])  # índice 0
    entregas = [(i+1, c) for i, c in enumerate(coordenadas[1:])]  # índice 1..n

    # Clusterizar solo las coordenadas, pero conservar índices
    coords_array = np.array([c for i, c in entregas])
    kmeans = KMeans(n_clusters=numRepartidores, random_state=0).fit(coords_array)
    
    clusters = [[] for _ in range(numRepartidores)]
    for (idx, coord), label in zip(entregas, kmeans.labels_):
        clusters[label].append((idx, coord))  # Guardar índice + coordenada

    # Agregar depósito al inicio
    rutas = []
    for cluster in clusters:
        ruta = [deposito] + cluster
        rutas.append(ruta)

    return rutas


def rutasOptimas(coordenadas, numRepartidores, grafo):
    #grafo = obtenerGrafoProyectado()
    
    rutas_cluster = agruparEntregasIndices(coordenadas, numRepartidores)
    rutas_finales = []

    for ruta in rutas_cluster:
        indices, coords = zip(*ruta)  # separar índices y coordenadas
        nodos = coordenadasANodos(coords, grafo)
        matriz = matrizDistancias(grafo, nodos)
        ruta_optima_idx = resolverTSP(matriz)
        
        # Devolver los índices originales de la lista completa
        ruta_optima_indices = [indices[i] for i in ruta_optima_idx]
        rutas_finales.append(ruta_optima_indices)

    return rutas_finales









