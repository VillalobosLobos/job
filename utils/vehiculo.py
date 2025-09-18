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
    """
    Cambia el status de un vehículo en el JSON.

    Parámetros:
        ruta : str
            Ruta del archivo JSON.
        tipo : str
            "motos" o "autos".
        idTransporte : str o int
            Id del vehículo a modificar.
        nuevoStatus : str
            Nuevo estado, por ejemplo "libre" u "ocupado".
    """
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
    
    print(f"Status del {tipo} id={idTransporte} cambiado a '{nuevoStatus}'")
    return True



