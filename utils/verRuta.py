import osmnx as ox
import itertools
import folium

def rutaFinal(rutaOptima, grafo):
    rutaFinalCompleta = []
    coords = []

    # Paleta de colores (se cicla si hay más tramos que colores)
    colores = itertools.cycle([
        "red", "blue", "green", "purple", "orange",
        "darkred", "lightblue", "darkgreen", "pink", "cadetblue"
    ])

    # Crear mapa centrado en el primer punto
    primerNodo = rutaOptima[0]
    mapa = folium.Map(location=[grafo.nodes[primerNodo]['y'], grafo.nodes[primerNodo]['x']], zoom_start=13)

    # Dibujar tramo por tramo
    for i in range(len(rutaOptima) - 1):
        nodoInicio = rutaOptima[i]
        nodoFin = rutaOptima[i+1]

        # Calcula la ruta más corta entre pares
        rutaCorta = ox.shortest_path(grafo, nodoInicio, nodoFin, weight='travel_time')

        # Convertir nodos en coordenadas
        coordsTramo = [(grafo.nodes[n]['y'], grafo.nodes[n]['x']) for n in rutaCorta]

        # Dibujar línea del tramo con color distinto
        folium.PolyLine(
            coordsTramo,
            color=next(colores),
            weight=5,
            opacity=0.9
        ).add_to(mapa)

        rutaFinalCompleta.extend(rutaCorta)

    # Marcar
    nombre = "Ezequiel"
    entrega = "auidifonos"
    for nodo in rutaOptima:
        lat, lon = grafo.nodes[nodo]['y'], grafo.nodes[nodo]['x']

        popup_html = f"""
        <b>Entrega {i+1}</b><br>
        Cliente: {nombre}<br>
        Producto: {entrega}
        """     

        folium.Marker(
            location=(lat, lon),
            popup=popup_html,
            icon=folium.DivIcon(html=f"""
                <div style="text-align: center; white-space: nowrap;">
                <div style="font-size: 20pt; color: black; line-height: 0;">📌</div>
                <div style="font-size: 10pt; font-weight: bold; margin-top: 5px;">{i+1}</div>
            </div>
            """)
        ).add_to(mapa)

    return mapa
