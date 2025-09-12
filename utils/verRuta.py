import osmnx as ox
import folium

def rutaFinal(rutaOptima, grafo):
    rutaFinalCompleta = []
    for i in range(len(rutaOptima) - 1):
        nodo_inicio = rutaOptima[i]
        nodo_fin    = rutaOptima[i+1]

        # Calcular ruta más corta
        rutaCorta = ox.shortest_path(grafo, nodo_inicio, nodo_fin, weight='travel_time')

        if i == 0:
            rutaFinalCompleta.extend(rutaCorta)
        else:
            rutaFinalCompleta.extend(rutaCorta[1:])

    # Convertir nodos a coordenadas (lat, lon)
    coords = [(grafo.nodes[n]['y'], grafo.nodes[n]['x']) for n in rutaFinalCompleta]

    # Crear mapa centrado en el primer punto
    m = folium.Map(location=coords[0], zoom_start=14)

    # Dibujar la ruta en azul más gruesa
    folium.PolyLine(coords, color="blue", weight=7, opacity=0.9).add_to(m)

    # Marcar cada punto en orden
    for i, nodo in enumerate(rutaOptima):
        lat, lon = grafo.nodes[nodo]['y'], grafo.nodes[nodo]['x']

        # Intentar obtener dirección del nodo
        direccion = grafo.nodes[nodo].get("name", "Dirección desconocida")

        # Marcador numerado + popup con dirección
        folium.Marker(
            location=(lat, lon),
            popup=f"<b>Punto {i+1} 🪀</b><br>{direccion}",
            icon=folium.DivIcon(html=f"""
                <div style="font-size: 12pt; color: black">{i+1}</div>
            """)
        ).add_to(m)

    return m
