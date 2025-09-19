import networkx as nx
import osmnx as ox
import time
import math
import os

lugares = [
    # Alcaldías CDMX
    "Álvaro Obregón, Ciudad de México, Mexico",
    "Azcapotzalco, Ciudad de México, Mexico",
    "Benito Juárez, Ciudad de México, Mexico",
    "Coyoacán, Ciudad de México, Mexico",
    "Cuajimalpa de Morelos, Ciudad de México, Mexico",
    "Cuauhtémoc, Ciudad de México, Mexico",
    "Gustavo A. Madero, Ciudad de México, Mexico",
    "Iztacalco, Ciudad de México, Mexico",
    "Iztapalapa, Ciudad de México, Mexico",
    "La Magdalena Contreras, Ciudad de México, Mexico",
    "Miguel Hidalgo, Ciudad de México, Mexico",
    "Milpa Alta, Ciudad de México, Mexico",
    "Tláhuac, Ciudad de México, Mexico",
    "Tlalpan, Ciudad de México, Mexico",
    "Venustiano Carranza, Ciudad de México, Mexico",
    "Xochimilco, Ciudad de México, Mexico",

    # Hidalgo
    "Tizayuca, Hidalgo, Mexico",

    # Municipios del Edomex (59)
    "Acolman, Mexico",
    "Amecameca, Mexico",
    "Apaxco, Mexico",
    "Atenco, Mexico",
    "Atizapán de Zaragoza, Mexico",
    "Atlautla, Mexico",
    "Axapusco, Mexico",
    "Ayapango, Mexico",
    "Coacalco de Berriozábal, Mexico",
    "Cocotitlán, Mexico",
    "Coyotepec, Mexico",
    "Cuautitlán, Mexico",
    "Chalco, Mexico",
    "Chiautla, Mexico",
    "Chicoloapan, Mexico",
    "Chiconcuac, Mexico",
    "Chimalhuacán, Mexico",
    "Ecatepec de Morelos, Mexico",
    "Ecatzingo, Mexico",
    "Huehuetoca, Mexico",
    "Hueypoxtla, Mexico",
    "Huixquilucan, Mexico",
    "Isidro Fabela, Mexico",
    "Ixtapaluca, Mexico",
    "Jaltenco, Mexico",
    "Jilotzingo, Mexico",
    "Juchitepec, Mexico",
    "Melchor Ocampo, Mexico",
    "Naucalpan de Juárez, Mexico",
    "Nezahualcóyotl, Mexico",
    "Nextlalpan, Mexico",
    "Nicolás Romero, Mexico",
    "Nopaltepec, Mexico",
    "Otumba, Mexico",
    "Ozumba, Mexico",
    "Papalotla, Mexico",
    "La Paz, Mexico",
    "San Martín de las Pirámides, Mexico",
    "Tecámac, Mexico",
    "Temamatla, Mexico",
    "Temascalapa, Mexico",
    "Tenango del Aire, Mexico",
    "Teoloyucan, Mexico",
    "Teotihuacán, Mexico",
    "Tepetlaoxtoc, Mexico",
    "Tepetlixpa, Mexico",
    "Tepotzotlán, Mexico",
    "Tequixquiac, Mexico",
    "Texcoco, Mexico",
    "Tezoyuca, Mexico",
    "Tlalmanalco, Mexico",
    "Tlalnepantla de Baz, Mexico",
    "Tonanitla, Mexico",
    "Tultepec, Mexico",
    "Tultitlán, Mexico",
    "Valle de Chalco Solidaridad, Mexico",
    "Villa del Carbón, Mexico",
    "Zumpango, Mexico",
    "Cuautitlán Izcalli, Mexico"
]

import os
import osmnx as ox

def generarGrafo():
    """
    Descarga un grafo de carreteras de la Zona Metropolitana del Valle de México
    usando graph_from_place y lo guarda en un archivo .graphml.
    """
    # Definir la zona a consultar
    zona = "Zona Metropolitana del Valle de México, México"

    print(f"Descargando el grafo de {zona}...")
    try:
        G = ox.graph_from_place(
            zona, 
            network_type="drive", 
            simplify=True,
            retain_all=False  # Mantener solo el componente gigante
        )
        
        # Crear carpeta si no existe
        os.makedirs("data", exist_ok=True)
        filepath = "data/zonaMetropolitana.graphml"

        # Guardar el grafo
        ox.save_graphml(G, filepath=filepath)
        print(f"Grafo de la Zona Metropolitana guardado en: {filepath}")

        return G

    except Exception as e:
        print(f"Ocurrió un error al generar el grafo: {e}")
        return None

def obtenerGrafo():
	print("\nEstamos carganfo el grafo ....")
	grafo = ox.load_graphml(filepath='data/zonaMetropolitana.graphml')
	return grafo
	
def generarGrafoCDMX():
	# Define the place you want to query.
	zona = "Ciudad de México, México"

	print(f"Descargando el grafo de {zona}...")
	try:
		G = ox.graph_from_place(
			zona, 
			network_type="drive", 
			simplify=True,
			retain_all=False
		)
        
		# Guardar el grafo en un archivo .graphml
		filepath = "data/zonaMetropolitana.graphml"
		ox.save_graphml(G, filepath=filepath)
        
		print(f"Grafo de CDMX guardado en: {filepath}")
		return G
	except Exception as e:
		print(f"Ocurrió un error al generar el grafo: {e}")
		return None






