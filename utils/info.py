'''
En este archivo vamos a leer las rutas del usuario de un cvs como:
id ruta
id cliente
nombre
productos
latiud 
longitud
idTipoPunto [1-> inicio , 2-> entrega, 3-> fin]
'''
from geopy.geocoders import Nominatim
import pandas as pd

def obtenerFinInicio(cont):
    inicio = cont[cont["tipoPunto"] == 1].iloc[0]
    fin = inicio#cont[cont["tipoPunto"] == 3].iloc[0]
    return [
        [float(inicio["latitud"]), float(inicio["longitud"])],
        [float(fin["latitud"]), float(fin["longitud"])]
    ]

#Para ver la dirección como dirección y no coordenadas
def direcciones(puntos):
	coordenada = f'{puntos[0]},{puntos[1]}'
	geolocalizacion = Nominatim(user_agent="direcciones") #Solo un nombre para buscar
	locacion = geolocalizacion.reverse(coordenada)
	return f"{locacion.address}"

def coordenadasLL(direccion):
	geolocalizacion = Nominatim(user_agent="direcciones") #Solo un nombre para buscar
	locacion = geolocalizacion.geocode(direccion)
	if locacion:
		print("La dirección es:", locacion.direccion)
		print("Latitud:", locacion.latitude)
		print("Longitud:", locacion.longitude)
	else:
		print(f'La dirección es: {direccion}')
		print("No se encontraron coordenadas para la dirección proporcionada.")

def obtenerPuntos(cont):
	entregas = cont[cont["tipoPunto"] == 2]
	coorEntregas = entregas[["latitud", "longitud"]].values.tolist()
	return coorEntregas

def obtenerCSV(ruta):
	cont = pd.read_csv(ruta)
	return cont

