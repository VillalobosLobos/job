from django.db import models

# Para poner el tipo de vehiculo, como carro, moto, camión de carga, etc...

class Tipos_de_vehiculos(models.TextChoices):
    #valor dentro la BD, valor que se mostrara en la etiqueta
    MOTO = 'moto', 'Carro'
    CARRO = 'carro', 'Moto'