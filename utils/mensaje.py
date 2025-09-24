def mensajeWhatssap(nombres, numeros, distTiempo, ruta, datos):
    consumoGasolina = distTiempo[0] / datos["kmPorLitro"]
    salida = f"Repartidor designado : {datos["repartidor"]}\nVehículo designado : {datos["modelo"]}\n\n"
    salida += f"🚚 Entrega programada\n\nInicias viaje en {nombres[0]}\n\n"
    for i in range(1,len(nombres)-1):
        salida += f'📍 Entrega {i}\n👤 Cliente : {nombres[i]}\n📞 Teléfono : {numeros[i]}\n\n'
    salida += f"Terminas viaje en {nombres[0]}\n\n"
    salida += f'Distancia aproximada : {distTiempo[0]}km.\nConsumo aprox. gasolina : {consumoGasolina:.3f}L.\nTiempo aproximado : {distTiempo[1]} minutos'
    salida += f'\n\n🚗 Ruta completa: \n{ruta}'
    return salida