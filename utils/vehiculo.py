import json

def mostrarVehiculos(motos, autos):
	salida = 'Motos:\n'
	for m in motos:
		salida = salida + '\t' + m[0] + '.- ' + m[1] + '\n'
	salida = salida + '\nAutos:\n'
	for a in autos:
		salida = salida + '\t' + a[0] + '.- ' + a[1] + '\n'
	return salida

def obtenerContenido(ruta):
	with open(ruta, "r", encoding="utf-8") as f:
		config = json.load(f)
	return config

def obtenerMotos(cont):
	salida = []
	for moto in cont["motos"]:
		if moto["status"] == "libre":
			salida.append([moto["id"], moto["modelo"], moto["rendimientoKML"]])
	return salida

def obtenerAutos(cont):
	salida = []
	for auto in cont["autos"]:
		if auto["status"] == "libre":
			salida.append([auto["id"], auto["modelo"], auto["rendimientoKML"]])
	return salida

def cambiarStatusVehiculo(ruta, tipo, idTransporte, nuevoStatus):
	# Cargar JSON
	with open(ruta, "r", encoding="utf-8") as f:
		data = json.load(f)

	# Buscar y modificar
	encontrado = False
	for vehiculo in data.get(tipo, []):
		if str(vehiculo["id"]) == str(idTransporte):
			vehiculo["status"] = nuevoStatus
			encontrado = True
			break

	if not encontrado:
		print(f"No se encontró {tipo} con id {idTransporte}")
		return False

	# Guardar JSON
	with open(ruta, "w", encoding="utf-8") as f:
		json.dump(data, f, indent=4, ensure_ascii=False)
		return True

def recuperarVehiculo(cont, ide, tipo):
	if tipo == "M":
		for moto in cont["motos"]:
			if moto["id"] == ide:
				return [moto["id"], moto["modelo"], moto["rendimientoKML"]]
	else:
		for auto in cont["autos"]:
			if auto["id"] == ide:
				return [auto["id"], auto["modelo"], auto["rendimientoKML"]]

def consumoGasolina(distancia, rendimiento):
	return distancia/rendimiento


