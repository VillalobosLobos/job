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
listaBeneficios = []
nombres = []
numeros = []

#g.generarGrafo()	
grafo = g.obtenerGrafoProyectado()


repartidores = menu.primerMenu()
noRepartidores = len(repartidores)

#g.generarGrafo()
#[[19.4256407, -99.1636657], [19.4256407, -99.1636657], [19.4218546, -99.1871364], [19.402751, -99.098584]]
coordenadas = [[19.4256407, -99.1636657], [19.4383482, -99.1017356], [19.4218546, -99.1871364], [19.402751, -99.098584]] #dirCoord.direccionACoordenadas(puntos)

ruta = g.rutasOptimas(coordenadas,noRepartidores, grafo)
print(ruta)

#os.system('clear')
aux = 0

for r in ruta:
	tiempoPorEntrega = 0

	for i in r:
		beneficios = cvs.obtenerBeneficios(contenido.iloc[i]["beneficios"], contenido.iloc[i]["costoBeneficios"])
		listaBeneficios.append(cvs.cadenaObtenerBeneficios(beneficios))
		nombres.append(contenido.iloc[i]["nombre"])
		numeros.append(contenido.iloc[i]["numTelefono"])
		noBeneficios = len(beneficios[0])
		tiempoPorEntrega += cvs.tiempoExtraPorEntrega(contenido.iloc[i]['tipoEntrega'], noBeneficios)
		rutaFinal.append(cvs.direccion(contenido.iloc[i]))

	url = urlG.generarLinkGoogleMaps(rutaFinal)
	distTiempo = [10,10]#dirCoord.calcularDistancia(rutaFinal)

	#Le sumamos el tiempo extra estimado por entrega
	distTiempo[1] += tiempoPorEntrega

	print(msj.mensajeWhatssap(nombres, numeros, distTiempo, url, repartidores[aux], listaBeneficios))
	print("\n\n")
	rutaFinal = []
	listaBeneficios = []
	nombres = []
	numeros = []
	aux+=1

