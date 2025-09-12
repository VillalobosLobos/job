import osmnx as ox

def generarGrafo():
    print("Descargando y creando el grafo...")
    grafo = ox.graph_from_place("Ciudad de México, Mexico", network_type='drive')
    ox.save_graphml(grafo, filepath='./grafo.graphml')
    print("Grafo guardado :D\n\n")

def cargarGrafo():
    print("Cargando el grafo desde el archivo...")
    grafo = ox.load_graphml(filepath='./grafo.graphml')
    print("Abra cadabra tarea terminada")
    return grafo
