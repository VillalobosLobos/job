import json

def obtenerContenido(ruta):
	with open(ruta, "r", encoding="utf-8") as f:
		config = json.load(f)
	return config

def obtenerMotos(cont):
	salida = []
	for moto in cont["motos"]:
		if moto["status"] == "libre":
			salida.append(moto["modelo"])
	return salida

def obtenerAutos(cont):
	salida = []
	for auto in cont["autos"]:
		if auto["status"] == "libre":
			salida.append(auto["modelo"])
	return salida

def modificarStatus(ruta, ide, tipo):
	cont = obtenerContenido(ruta)
	if tipo == 'M':#Moto
		for moto in cont["motos"]:
			if moto["id"] == ide:
				moto["status"] == "ocupado"
				break
	else:#Auto
		for auto in cont["autos"]:
			if auto["id"] == ide:
				auto["status"] == "ocupado"
				break

	with open("confVehiculo.json", "w", encoding="utf-8") as f:
		json.dump(cont, f, indent=4, ensure_ascii=False)



