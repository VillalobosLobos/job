from utils.generarGrafo import generarGrafo
from utils.generarGrafo import cargarGrafo
from utils.ruta import ruta
import os

os.system("clear")

generarGrafo()
grafo = cargarGrafo()

#Puntos para optimizar ruta
inicio = (19.426991 , -99.160783)
puntos = [
    (19.435982 , -99.154387), #Monumneto a la revolución
    (19.433132 , -99.134274), #zocalo
    (19.485127 , -99.118516) , #bascilica
    (19.544969 , -99.017376)

]

ruta(inicio, puntos, grafo)

print("######## Vamonos recio ########")

