from django.db import models

# Para el tipo de licencia, como de moto o carro

class Tipos_de_licencias(models.TextChoices):
    #valor dentro la BD, valor que se mostrara en la etiqueta
    LICENCIA_PARA_MOTO = 'licencia_moto' , 'Licencia para moto'
    LICENCIA_PARA_CARRO = 'licencia_carro', 'Licencia para carro'