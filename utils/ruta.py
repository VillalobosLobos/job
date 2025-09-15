from networkx.algorithms import approximation
from utils.verRuta import rutaFinal
import networkx as nx
import osmnx as ox
import requests
from datetime import datetime, timedelta

API_KEY = "AIzaSyCmdGm34HbPnfTdtgXNMERWPpxxOB9j0uQ"

def obtenerTiempoTrafico(origen, destino):
    #Para especificar el medio de transporte DRIVE (carros) y TWO_WHEELER (motos) peeero está en beta
    transporte = "DRIVE"

    #Regresa duración en segundos considerando tráfico en tiempo real usando Google Routes API.
    url = "https://routes.googleapis.com/directions/v2:computeRoutes"

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": "routes.duration"
    }

    body = {
        "origin": {"location": {"latLng": {"latitude": origen[0], "longitude": origen[1]}}},
        "destination": {"location": {"latLng": {"latitude": destino[0], "longitude": destino[1]}}},
        "travelMode": transporte,
        "routingPreference": "TRAFFIC_AWARE_OPTIMAL",
        "departureTime": (datetime.utcnow() + timedelta(minutes=5)).isoformat("T") + "Z" #Vamos 5 minutos al futuro
    }

    resp = requests.post(url, headers=headers, json=body)

    if resp.status_code == 200:
        data = resp.json()
        if "routes" in data and len(data["routes"]) > 0:
            duration_str = data["routes"][0]["duration"]
            return int(duration_str.replace("s", ""))
    else:
        print("Error API:", resp.text)

    return None

def TSP(grafoNuevo, nodosVisitas):
    rutaOptima = approximation.traveling_salesman_problem(
        grafoNuevo, nodes=nodosVisitas
    )
    print("Ruta óptima")
    return rutaOptima

def crearNuevoGrafo(distancias):
    grafoNuevo = nx.DiGraph() #Crea un grafo dirigido
    for (val1, val2), distancia in distancias.items():
        #Añade la nueva arista
        grafoNuevo.add_edge(val1, val2, weight=distancia)
    print("Grafo creado")
    return grafoNuevo

def distanciasVisitas(nodosVisitas, grafo):
    distancias = {}

    #Para comparar un punto con todos los demás, distancia
    for val1 in nodosVisitas:
        for val2 in nodosVisitas:
            if val1 != val2:
                lat1, lon1 = grafo.nodes[val1]["y"], grafo.nodes[val1]["x"]
                lat2, lon2 = grafo.nodes[val2]["y"], grafo.nodes[val2]["x"]

                #Obtenemos el tiempo de A a B considerando el tráfico
                tiempo = obtenerTiempoTrafico((lat1, lon1), (lat2, lon2))
                if tiempo:
                    distancias[(val1, val2)] = tiempo
    print("Distancias con tráfico obtenidas")
    return distancias

def ruta(puntoInicio, puntosVisitas, grafo):
    visitas = puntosVisitas + [puntoInicio]

    # Añadir velocidades y tiempos base (OSMnx)
    grafo = ox.add_edge_speeds(grafo)
    grafo = ox.add_edge_travel_times(grafo)

    # Obtener nodos más cercanos
    nodosVisitas = []   
    for latitud, longitud in visitas:
        nodoMasCercano = ox.distance.nearest_nodes(grafo, longitud, latitud)
        nodosVisitas.append(nodoMasCercano)
    
    # Distancias con tráfico real
    distancias = distanciasVisitas(nodosVisitas, grafo)
    if not distancias:
        raise ValueError("No se obtuvo la distancia con tráfico")

    grafoNuevo = crearNuevoGrafo(distancias)
    rutaOptima = TSP(grafoNuevo, nodosVisitas)

    m = rutaFinal(rutaOptima, grafo)
    m.save("ruta.html")
