import utils.catalogos as catalogo
import os

#Rutas a los archivos
RUTA_CATALOGO_CARROS = "catalogos/carros.json"
RUTA_CATALOGO_MOTOS = "catalogos/motos.json"
RUTA_CATALOGO_REPARTIDORES = "catalogos/repartidores.json"

def primerMenu():
    catalogo.resetVehiculos(RUTA_CATALOGO_CARROS)
    catalogo.resetVehiculos(RUTA_CATALOGO_MOTOS)

    numRepart = menuRepartidores()
    print(numRepart)
    ids = catalogo.idRepartidores(RUTA_CATALOGO_REPARTIDORES)

    if numRepart != -1 and catalogo.idValidos(ids, numRepart):
        for i in range(len(numRepart)):
            os.system('clear')
            repartidor = catalogo.obtenerRepartidorPorId(numRepart[i], RUTA_CATALOGO_REPARTIDORES)
            licencias = catalogo.obtenerLicencias(repartidor)
            tieneLicencia = menuVehiculosDisponibles(licencias, repartidor)
            if tieneLicencia:
                print('\nQué vehículo se le va a asignar? ',end='')
                idVehiculo = int(input())

                catalogo.asignarRepartidorAVehiculo(numRepart[i], idVehiculo, RUTA_CATALOGO_CARROS, RUTA_CATALOGO_MOTOS)
            else:
                print('\n\nMejor dile que obtenga su licencia ☠️')

        #Una vez asignado vehiculo y repartidos
        #return catalogo.obtenerRepartidoresOcupados(RUTA_CATALOGO_CARROS, RUTA_CATALOGO_MOTOS)
        #return catalogo.obtenerCarrosOcupados(RUTA_CATALOGO_CARROS)
        return catalogo.obtenerVehiculosOcupados(RUTA_CATALOGO_CARROS, RUTA_CATALOGO_MOTOS, RUTA_CATALOGO_REPARTIDORES)

def menuVehiculosDisponibles(licencias, repartidor):
    carros = catalogo.obtenerContenido(RUTA_CATALOGO_CARROS)['carros']
    motos = catalogo.obtenerContenido(RUTA_CATALOGO_MOTOS)['motos']

    print(f'\nRepartidor elegido {repartidor["nombre"]}\n')

    opciones = []  # lista de vehículos que sí puede manejar

    if licencias[1]:  # carro
        disponibles = catalogo.obtenerCarrosDisponibles(carros)
        if disponibles:
            print('\nCarros disponibles:')
            for carro in disponibles:
                print(f'- (Id = {carro["id"]}) {carro["modelo"]}')
                opciones.append(carro["id"])
        else:
            print("\nNo hay carros disponibles ahora mismo")
    else:
        print('\nNo cuenta con licencia para manejar carro')

    if licencias[0]:  # moto
        disponibles = catalogo.obtenerMotosDisponibles(motos)
        if disponibles:
            print('\nMotos disponibles:')
            for moto in disponibles:
                print(f'- (Id = {moto["id"]}) {moto["modelo"]}')
                opciones.append(moto["id"])
        else:
            print("\nNo hay motos disponibles ahora mismo")
    else:
        print('\nNo cuenta con licencia para manejar moto')

    return opciones  # devuelves la lista de IDs disponibles

def menuRepartidores():
    os.system('clear')
    repartidoresLibres = catalogo.obtenerRepartidoresDisponibles(RUTA_CATALOGO_CARROS,RUTA_CATALOGO_MOTOS,RUTA_CATALOGO_REPARTIDORES)

    print(f'Los repartidores libres son :')
    for repartidor in repartidoresLibres:
        print(f' - (Id = {repartidor['id']}) {repartidor['nombre']}')
    
    print('\nSelecciones los Id de los repartidores que asignara ruta separados por coma: ',end='')
    ids = input()
    numReparConDuplicados = ids.split(',')
    numReparSinDuplicado = set(numReparConDuplicados)
    numRepar = list(numReparSinDuplicado)
    numRepar = [int(num) for num in numRepar]

    if len(numRepar) <= len(repartidoresLibres):
        return numRepar
    else:
        print('\nNo están disponibles :(\n')
        return -1