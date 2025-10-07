from django.db import models

#Para saber si la entrega esta: pendiente, terminada o reagendada

class Estados_de_entregas(models.TextChoices):
    #valor dentro la BD, valor que se mostrara en la etiqueta
    PENDIENTE = 'pendiente', 'Pendiente'
    TERMINADA = 'terminada', 'Terminada'
    REAGENDADA = 'reagendada', 'Reagendada'