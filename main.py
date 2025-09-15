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

# Puntos a no más de 20 metros del Zócalo
puntos2 = [
    # En la plancha del Zócalo
    (19.432608, -99.133290),  # 1. Centro del Zócalo
    (19.432650, -99.133100),  # 2. Esquina Noreste del Zócalo
    (19.432450, -99.133200),  # 3. Esquina Sureste del Zócalo
    (19.432550, -99.133400),  # 4. Esquina Suroeste del Zócalo
    (19.432750, -99.133300),  # 5. Esquina Noroeste del Zócalo
    
    # Alrededor del Zócalo
    (19.432600, -99.133400),  # 6. Frente a la Suprema Corte
    (19.432450, -99.133150),  # 7. Frente al Antiguo Palacio del Ayuntamiento
    (19.432750, -99.133250),  # 8. Entrada del Palacio Nacional
    (19.432850, -99.133100),  # 9. Entrada de la Catedral Metropolitana
    (19.432900, -99.133000),  # 10. Campanario de la Catedral
    
    # Puntos adicionales cercanos
    (19.432300, -99.133050),  # 11. Edificio de Gobierno (esquina 20 de Noviembre)
    (19.432200, -99.133150),  # 12. Calle 5 de Febrero (lado sur)
    (19.432800, -99.133450),  # 13. Calle 5 de Mayo (lado norte)
    (19.433050, -99.133200),  # 14. Templo de San Felipe Neri (detrás de la Catedral)
    (19.432100, -99.132950),  # 15. Esquina Pino Suárez
    (19.432500, -99.132950),  # 16. Esquina Moneda
    (19.432600, -99.132800),  # 17. Esquina Seminario (Templo Mayor)
    (19.432750, -99.133000),  # 18. Calle Guatemala (detrás de la Catedral)
    (19.432800, -99.133150),  # 19. Plaza de las Culturas (interior)
    (19.432550, -99.133200),  # 20. Punto intermedio en la plancha
]

Tinicio = time.time()
ruta(inicio, puntos, grafo)
Tfin = time.time()
print(f'No. Puntos {len(puntos) + 1} tardo : {Tfin-Tinicio}')
