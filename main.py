from utils.generarGrafo import generarGrafo, cargarGrafo
from utils.ruta import ruta
import os
import time

os.system("clear")

#generarGrafo()
grafo = cargarGrafo()

# Punto de inicio
inicio = (19.426991, -99.160783)  # Ángel de la independencia

# Puntos para optimizar ruta
puntos = [
    (19.435982, -99.154387),  # Monumento a la Revolución
    (19.433132, -99.134274),  # Zócalo
    (19.485127, -99.118516),  # Basílica
]

puntos2 = [
    (19.435982, -99.154387),  # 1. Monumento a la Revolución
    (19.433132, -99.134274),  # 2. Zócalo / Plaza de la Constitución
    (19.485127, -99.118516),  # 3. Basílica de Guadalupe
    (19.426214, -99.135246),  # 4. Palacio de Bellas Artes
    (19.421695, -99.131102),  # 5. Templo Mayor
    (19.431268, -99.179374),  # 6. Castillo de Chapultepec
    (19.426831, -99.186646),  # 7. Museo Nacional de Antropología
    (19.427027, -99.167735),  # 8. Ángel de la Independencia
    (19.349633, -99.165207),  # 9. Museo Frida Kahlo (Casa Azul)
    (19.435306, -99.133276),  # 10. Alameda Central
    (19.412850, -99.168536),  # 11. Museo Soumaya
    (19.317540, -99.130310),  # 12. Estadio Azteca
    (19.432608, -99.133290),  # 13. Torre Latinoamericana
    (19.351658, -99.141876),  # 14. Mercado de Coyoacán
    (19.317926, -99.176412),  # 15. Ciudad Universitaria (UNAM)
    (19.436159, -99.144933),  # 16. Kiosco Morisco
    (19.418721, -99.172901),  # 17. Auditorio Nacional
    (19.434380, -99.141430),  # 18. Hemiciclo a Juárez
    (19.436048, -99.139627),  # 19. Museo de Memoria y Tolerancia
    (19.333038, -99.184347),  # 20. Jardín Centenario (Coyoacán)
]

Tinicio = time.time()
ruta(inicio, puntos2, grafo)
Tfin = time.time()
print(f'No. Puntos {len(puntos) + 1} tardo : {Tfin-Tinicio}')
