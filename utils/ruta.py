from networkx.algorithms import approximation
from utils.verRuta import rutaFinal
import networkx as nx
import osmnx as ox
import requests
from datetime import datetime, timedelta

API_KEY = "AIzaSyCmdGm34HbPnfTdtgXNMERWPpxxOB9j0uQ"

# ------------------------------
# 🔹 Función usando Google API
# ------------------------------
def obtenerTiempoTrafico(origen, destino):
    transporte = "DRIVE"  # "TWO_WHEELER" si quieres moto (beta)

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
        "departureTime": (datetime.utcnow() + timedelta(minutes=5)).isoformat("T") + "Z"
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


def distanciasVisitas_API(nodosVisitas, grafo):
    distancias = {}
    for val1 in nodosVisitas:
        for val2 in nodosVisitas:
            if val1 != val2:
                lat1, lon1 = grafo.nodes[val1]["y"], grafo.nodes[val1]["x"]
                lat2, lon2 = grafo.nodes[val2]["y"], grafo.nodes[val2]["x"]
                tiempo = obtenerTiempoTrafico((lat1, lon1), (lat2, lon2))
                if tiempo:
                    distancias[(val1, val2)] = tiempo
    print("Distancias con tráfico obtenidas (API)")
    return distancias


# ------------------------------
# 🔹 Función SIN API (solo OSMnx)
# ------------------------------
def distanciasVisitas_OSM(nodosVisitas, grafo):
    distancias = {}
    for val1 in nodosVisitas:
        for val2 in nodosVisitas:
            if val1 != val2:
                try:
                    # Tiempo más corto en base a OSMnx (sin tráfico)
                    tiempo = nx.shortest_path_length(
                        grafo, source=val1, target=val2, weight="travel_time"
                    )
                    distancias[(val1, val2)] = tiempo
                except Exception:
                    continue
    print("Distancias obtenidas con OSMnx (sin API)")
    return distancias


# ------------------------------
# 🔹 Funciones comunes
# ------------------------------
def TSP(grafoNuevo, nodosVisitas):
    rutaOptima = approximation.traveling_salesman_problem(
        grafoNuevo, nodes=nodosVisitas
    )
    print("Ruta óptima encontrada")
    return rutaOptima


def crearNuevoGrafo(distancias):
    grafoNuevo = nx.DiGraph()
    for (val1, val2), distancia in distancias.items():
        grafoNuevo.add_edge(val1, val2, weight=distancia)
    return grafoNuevo


# ------------------------------
# 🔹 Función principal con selector
# ------------------------------
def ruta(puntoInicio, puntosVisitas, grafo, usar_api=True):
    visitas = puntosVisitas + [puntoInicio]

    # Añadir velocidades y tiempos base (OSMnx)
    grafo = ox.add_edge_speeds(grafo)
    grafo = ox.add_edge_travel_times(grafo)

    # Obtener nodos más cercanos
    nodosVisitas = []
    for latitud, longitud in visitas:
        nodoMasCercano = ox.distance.nearest_nodes(grafo, longitud, latitud)
        nodosVisitas.append(nodoMasCercano)

    # ------------------
    # Distancias según modo
    # ------------------
    #if usar_api:
    #    distancias = distanciasVisitas_API(nodosVisitas, grafo)
    #else:
    #    distancias = distanciasVisitas_OSM(nodosVisitas, grafo)
    distancias = distanciasVisitas_OSM(nodosVisitas, grafo)

    if not distancias:
        raise ValueError("No se pudieron obtener distancias")

    grafoNuevo = crearNuevoGrafo(distancias)
    rutaOptima = TSP(grafoNuevo, nodosVisitas)

    m = rutaFinal(rutaOptima, grafo)
    m.save("ruta.html")
    print("Ruta guardada en ruta.html ✅")
