from dotenv import load_dotenv
import urllib.parse
import requests
import json
import os

#Cargar las variables de entorno
load_dotenv()

API_KEY = os.getenv("API_KEY_GOOGLE_MAPS")

def direccionACoordenadas(direcciones):
	coordenadas = []
	url = "https://maps.googleapis.com/maps/api/geocode/json"

	for direccion in direcciones:
		parametros = {
			'address': direccion,
			'key': API_KEY,
			'language': 'es',
			'region': 'mx'
		}

		try:
			response = requests.get(url, params = parametros)
			response.raise_for_status()
			info = response.json()

			if info['status'] == 'OK':
				resultado = info['results'][0]
				latitud = resultado['geometry']['location']['lat']
				longitud = resultado['geometry']['location']['lng']
				coordenadas.append([latitud,longitud])
			else:#Error en la API, mostramos mensaje de error
				print(f"Mensaje: {data['error_message']}")
		except Exception as e:
			print(f'Error: {e}\n')
	return coordenadas

def calcularDistancia(puntos, modoViaje="driving"):
    origen = urllib.parse.quote(puntos[0])
    destino = urllib.parse.quote(puntos[-1])

    if len(puntos) > 2:
        waypoints = "|".join([urllib.parse.quote(p) for p in puntos[1:-1]])
        url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origen}&destination={destino}&waypoints={waypoints}&mode={modoViaje}&key={API_KEY}"
    else:
        url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origen}&destination={destino}&mode={modoViaje}&key={API_KEY}"

    response = requests.get(url).json()

    if response["status"] == "OK":
        distancia_total = sum(leg["distance"]["value"] for leg in response["routes"][0]["legs"])
        duracion_total = sum(leg["duration"]["value"] for leg in response["routes"][0]["legs"])

        return [round(distancia_total / 1000, 2), round(duracion_total / 60, 1)]
    else:
        return {"error": response["status"]}







