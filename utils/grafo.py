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

def descargarGrafo(nombre):
    #Descarga el grafo de un municipio y lo guarda en disco
	nombreArchivo = f"data/grafos_zmvm/{nombre.replace(',', '').replace(' ', '_')}.graphml"
	if os.path.exists(nombreArchivo):
		print(f"Ya existe: {nombre}")
		return ox.load_graphml(nombreArchivo)
	try:
		print(f"Descargando: {nombre} ...")
		grafo = ox.graph_from_place(nombre, network_type="drive", simplify=True)
		ox.save_graphml(grafo, nombreArchivo)
		print(f":D Guardado: {nombreArchivo}")
		return grafo
	except Exception as e:
		print(f":( Error en {nombre}: {e}")
		return None

def procesarLote(lote, idx):
    #Procesa un lote de municipios
	print(f"\nProcesando lote {idx+1} ({len(lote)} lugares)")
	GLote = None
	for lugar in lote:
		grafo = descargarGrafo(lugar)
		if grafo is None:
			continue
		if GLote is None:
			GLote = grafo
		else:
			GLote = nx.compose(GLote, grafo)
		time.sleep(1)  # evitar saturar OSM
	if GLote:
		ox.save_graphml(GLote, f"data/grafos_zmvm/lote_{idx+1}.graphml")
		print(f"Lote {idx+1} guardado")
	return GLote

def generarGrafo():
	# Carpeta de guardado temporal
	os.makedirs("data/grafos_zmvm", exist_ok=True)
	tamLote = 10 #Para no gastar tanta RAM de 10 en 10
	lotes = [lugares[i:i+tamLote] for i in range(0, len(lugares), tamLote)]

	#Procesar cada lote
	grafosLotes = []
	for i, lote in enumerate(lotes):
		GLote = procesarLote(lote, i)
		if GLote:
			grafosLotes.append(GLote)

	# Unir todos los lotes
	GFinal = None
	for grafo in grafosLotes:
		if GFinal is None:
			GFinal = grafo
		else:
			GFinal = nx.compose(GFinal, grafo)

	if GFinal:
		ox.save_graphml(GFinal, "data/zonaMetropolitana.graphml")
		return "\nGrafo final guardado: zonaMetropolitana.graphml"

def obtenerGrafo():
	grafo = ox.load_graphml(filepath='data/zonaMetropolitana.graphml')
	return grafo
	







