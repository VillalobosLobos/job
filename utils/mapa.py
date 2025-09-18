import matplotlib.colors as colors
import matplotlib.cm as cm
import networkx as nx
import folium

def dibujarRutaMapa(nuevo, grafoProyectado, rutaOptima, rutaNodos, transformador, nombreArchivo="rutaOptima.html"):
    """
    Dibuja la ruta óptima en Folium con colores por segmento y marcadores de clientes.
    
    Parámetros:
        nuevo : pd.DataFrame
            DataFrame con clientes y nodos.
        grafoProyectado : networkx.MultiDiGraph
            Grafo proyectado.
        rutaOptima : list
            Orden de los índices de los clientes según TSP.
        rutaNodos : list
            Lista completa de nodos de la ruta.
        transformador : pyproj.Transformer
            Transformador de CRS proyectado a WGS84.
        nombreArchivo : str
            Nombre del archivo HTML donde se guardará el mapa.
    """
    # Centro del mapa
    latCentro = nuevo['latitud'].mean()
    lonCentro = nuevo['longitud'].mean()
    mapa = folium.Map(location=[latCentro, lonCentro], zoom_start=13)

    # Colores por segmento
    numSegmentos = len(rutaOptima)-1
    colormap = cm.get_cmap('tab10', numSegmentos)
    colores = [colors.rgb2hex(colormap(i)) for i in range(numSegmentos)]

    # Dibujar cada segmento de la ruta
    for i in range(len(rutaOptima)-1):
        inicioNodo = nuevo.loc[rutaOptima[i], 'nodo']
        finNodo = nuevo.loc[rutaOptima[i+1], 'nodo']
        camino = nx.shortest_path(grafoProyectado, inicioNodo, finNodo, weight='length')
        
        rutaSegmento = [
            transformador.transform(grafoProyectado.nodes[n]['x'], grafoProyectado.nodes[n]['y'])[::-1]
            for n in camino
        ]
        folium.PolyLine(rutaSegmento, color=colores[i], weight=5, opacity=0.8).add_to(mapa)

    # Marcador inicio/fin
    inicioIdx = rutaOptima[0]
    folium.Marker(
        location=[nuevo.loc[inicioIdx,'latitud'], nuevo.loc[inicioIdx,'longitud']],
        popup="🏁 Inicio/Fin 🏁",
        icon=folium.Icon(color='green', icon='play')
    ).add_to(mapa)

    # Marcadores de clientes con nombre + productos
    for orden, idx in enumerate(rutaOptima[1:-1], start=1):
        cliente = nuevo.loc[idx,'nombreCliente']
        productos = nuevo.loc[idx,'productos']
        folium.Marker(
            location=[nuevo.loc[idx,'latitud'], nuevo.loc[idx,'longitud']],
            popup=f"Parada {orden}. \n{cliente}\nProductos: {productos}",
            icon=folium.DivIcon(html=f"""<div style="font-size:15pt; color:black">📌{orden}</div>""")
        ).add_to(mapa)

    # Guardar mapa
    mapa.save(nombreArchivo)
    print(f"Mapa guardado: {nombreArchivo}")
