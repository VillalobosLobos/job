from datetime import datetime, timedelta
import requests

API_KEY = "AIzaSyCmdGm34HbPnfTdtgXNMERWPpxxOB9j0uQ"

def obtenerCasetaYTiempo(origen, destino, horaSalida):
	url = "https://maps.googleapis.com/maps/api/directions/json"
	params = {
		"origin": f"{origen[0]},{origen[1]}",
		"destination": f"{destino[0]},{destino[1]}",
		"departure_time": int(horaSalida.timestamp()),
		"key": API_KEY,
		"mode": "driving"
	}
	resp = requests.get(url, params=params).json()

	if not resp.get("routes"):  #Si está vacío
		print("No se encontró ruta entre:", origen, destino)
		return None, None

	leg = resp["routes"][0]["legs"][0]
	duracion = leg["duration_in_traffic"]["value"]  # en segundos
	
	# Si existe costo de caseta
	costo = None
	if "fare" in resp["routes"][0]:
		costo = resp["routes"][0]["fare"]["value"]  # en moneda local (ej: pesos MXN)

	return duracion, costo


