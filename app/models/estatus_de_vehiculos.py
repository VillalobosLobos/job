from django.db import models

#Para marcar cuando un vehiculo está : ocupado , libre, etc.

class Estatus_de_vehiculos(models.TextChoices):
    #valor dentro la BD, valor que se mostrara en la etiqueta
    LIBRE = 'libre', 'Libre'
    OCUPADO = 'ocupado', 'Ocupado'