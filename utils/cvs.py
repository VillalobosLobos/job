import pandas as pd
import math

def obtenerContenidoCVS(ruta):
	df = pd.read_csv(ruta)
	return df

def direccion(fila):
	datos = [fila["calle"], fila["numExt"], fila["numInt"], fila["colonia"], fila["deleMuni"],fila["cp"], fila["pais"]]
	limpios = [str(d) for d in datos if not (isinstance(d, float) and math.isnan(d))]
	direccion = ",".join(limpios)
	return direccion

#Recuerda df = data frame
def obtenerDirecciones(df):
	direcciones = []
	for indice, fila in df.iterrows():
		direcciones.append(direccion(fila))
	return direcciones