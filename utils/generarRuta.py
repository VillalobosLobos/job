import urllib.parse

def generarLinkGoogleMaps(puntos, modoViaje = "driving"):
	if len(puntos) < 2:
		return "Se necesitan 2 puntos o más para generar la ruta"
	elif len(puntos) > 2:
		paradasIntermedias = puntos[1:-1]
		interCodificados = []

		#Con esto codificamos espacios y comas para que funcione en el link
		origen = urllib.parse.quote(puntos[0])
		destino = urllib.parse.quote(puntos[-1])

		for punto in paradasIntermedias:
			interCodificados.append(urllib.parse.quote(punto))

		#Para unir todos los puntos para google Maps
		waypoints = "|".join(interCodificados)

		url = f'https://www.google.com/maps/dir/?api=1&origin={origen}&destination={destino}&travelmode={modoViaje}'
		url += f'&waypoints={waypoints}'

		return url
	else:
		return "Algo fallo ..."

