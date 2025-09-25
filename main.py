import utils.direccionACoordenada as dirCoord
import utils.catalogos as catalogo
import utils.generarRuta as urlG
import utils.mensaje as msj
import utils.menus as menu
import utils.grafo as g
import utils.cvs as cvs
import os

contenido = cvs.obtenerContenidoCVS("data/archivoCSV.csv")
puntos = cvs.obtenerDirecciones(contenido)
rutaFinal = []
nombres = []
numeros = []	
grafo = g.obtenerGrafoProyectado()


repartidores = menu.primerMenu()
noRepartidores = len(repartidores)
print(repartidores)


#g.generarGrafo()
#[[19.4256407, -99.1636657], [19.4256407, -99.1636657], [19.4218546, -99.1871364], [19.402751, -99.098584]]
coordenadas = dirCoord.direccionACoordenadas(puntos)

ruta = g.rutasOptimas(coordenadas,noRepartidores, grafo)

os.system('clear')
aux = 0
for r in ruta:
	for i in r:
		nombres.append(contenido.iloc[i]["nombre"])
		numeros.append(contenido.iloc[i]["numTelefono"])
		rutaFinal.append(cvs.direccion(contenido.iloc[i]))

	url = urlG.generarLinkGoogleMaps(rutaFinal)
	distTiempo = dirCoord.calcularDistancia(rutaFinal)

	print(msj.mensajeWhatssap(nombres, numeros, distTiempo, url, repartidores[aux]))
	print("\n\n")
	rutaFinal = []
	nombres = []
	numeros = []
	aux+=1

