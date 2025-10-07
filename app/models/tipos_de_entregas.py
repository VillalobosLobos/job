from django.db import models

#Para definir los tipos de entrega como: campo, masivo, etc...

class Tipos_de_entregas(models.TextChoices):
    #valor dentro la BD, valor que se mostrara en la etiqueta
    CAMPO = 'campo', 'Campo'
    MASIVO = 'masivo', 'Masivo'

