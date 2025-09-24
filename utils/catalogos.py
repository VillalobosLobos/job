import json

################## Solo repartidores ###############################

def obtenerRepartidoresOcupados(rutaC, rutaM):
    carros = obtenerContenido(rutaC)['carros']
    motos = obtenerContenido(rutaM)['motos']
    idReparOcupados = []
    for carro in carros:
        if carro['estatus'] == 'ocupado':
            idReparOcupados.append(carro['idConductor'])
    for moto in motos:
        if moto['estatus'] == 'ocupado':
            idReparOcupados.append(moto['idConductor'])
    return idReparOcupados

def obtenerRepartidoresDisponibles(rutaC,rutaM,rutaR):
    repartidores = obtenerContenido(rutaR)['repartidores']

    #Primero vamos a obtener los que no estan disponibles
    idReparOcupados = obtenerRepartidoresOcupados(rutaC, rutaM)

    idReparLibres = []
    for repartidor in repartidores:
        if repartidor['id'] not in idReparOcupados:
            idReparLibres.append(repartidor)
    return idReparLibres

def idRepartidores(ruta):
    ids = []
    repartidores = obtenerContenido(ruta)["repartidores"]
    for repartidor in repartidores:
        ids.append(repartidor["id"])
    return ids

def idValidos(ids, idsIngresados):
    for id in idsIngresados:
        if id not in ids:
            return False
    return True

def obtenerRepartidorPorId(id, ruta):
    repartidores = obtenerContenido(ruta)["repartidores"]
    for repartidor in repartidores:
        if repartidor['id'] == id:
            return repartidor
    return "No se encontro repartidor"

def obtenerLicencias(repartidor):
    licM = repartidor['licencias']['moto']
    licA = repartidor['licencias']['carro']
    return [licM, licA]

def asignarRepartidorAVehiculo(idRepartidor, idVehiculo, rutaC, rutaM):
    if 100 < idVehiculo < 200:  # carro
        ruta = rutaC
        data = obtenerContenido(ruta)
        cont = data['carros']
    elif 200 < idVehiculo < 300:  # moto
        ruta = rutaM
        data = obtenerContenido(ruta)
        cont = data['motos']
    else:
        print("ID de vehículo inválido")
        return

    for v in cont:
        if v["estatus"] == 'libre' and v["idConductor"] is None:
            v["estatus"] = 'ocupado'
            v["idConductor"] = idRepartidor
            break
    subirContenido(ruta, data)

##################    Solo motos     ###############################

def obtenerMotosDisponibles(contenido):
    libres = []
    for moto in contenido:
        if moto['estatus'] == 'libre':
            libres.append(moto)
    return libres

def obtenerMotosOcupadas(rutaM):
    contenido = obtenerContenido(rutaM)['motos']
    ocupados = []
    for moto in contenido:
        if moto["estatus"] == "ocupado":
            ocupados.append(
                {
                    "modelo": moto["modelo"],
                    "kmPorLitro": moto["kmPorLitro"],
                    "idConductor": moto["idConductor"]
                }
            )
    return ocupados

##################    Solo carros    ###############################

def obtenerCarrosDisponibles(contenido):
    libres = []
    for carro in contenido:
        if carro['estatus'] == 'libre':
            libres.append(carro)
    return libres

def obtenerCarrosOcupados(rutaC):
    contenido = obtenerContenido(rutaC)['carros']
    ocupados = []
    for carro in contenido:
        if carro["estatus"] == "ocupado":
            ocupados.append(
                {
                    "modelo": carro["modelo"],
                    "kmPorLitro": carro["kmPorLitro"],
                    "idConductor": carro["idConductor"]
                }
            )
    return ocupados

##################   sin categoría   ###############################

def obtenerContenido(ruta):
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

def subirContenido(ruta, data):
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def resetVehiculos(ruta):
    cont = obtenerContenido(ruta)

    for tipo, lista in cont.items():
        for v in lista:
            v["estatus"] = "libre"
            v["idConductor"] = None

    subirContenido(ruta, cont)

    print(f"Todos los vehículos en {ruta} fueron liberados.")

import json

def obtenerVehiculosOcupados(path_carros, path_motos, path_repartidores):
    # Cargar datos desde los archivos JSON
    with open(path_carros, "r", encoding="utf-8") as f:
        carros = json.load(f)["carros"]
    with open(path_motos, "r", encoding="utf-8") as f:
        motos = json.load(f)["motos"]
    with open(path_repartidores, "r", encoding="utf-8") as f:
        repartidores = json.load(f)["repartidores"]

    # Pasar lista de repartidores a dict {id: nombre}
    dict_repartidores = {r["id"]: r["nombre"] for r in repartidores}

    # Combinar carros y motos en una lista de vehículos
    vehiculos = carros + motos

    # Filtrar solo los ocupados y mapear la info deseada
    ocupados = []
    for v in vehiculos:
        if v["estatus"] == "ocupado" and v["idConductor"] is not None:
            ocupados.append({
                "modelo": v["modelo"],
                "kmPorLitro": v["kmPorLitro"],
                "repartidor": dict_repartidores.get(v["idConductor"], "Desconocido")
            })

    return ocupados




