from .tipos_de_licencias import Tipos_de_licencias
from .repartidores import Repartidores
from django.db import models

'''
Se hace referencia a el repatidor y al tipo de licencia,
donde si se elimina el repartidor o tipos de licencia se
eliminan las licencias
'''

class Licencias_de_repartidor(models.Model):
    id = models.AutoField(primary_key = True)
    id_repartidor = models.ForeignKey(Repartidores, on_delete = models.CASCADE)
    tipo_de_licencia = models.CharField(
        max_length = 20,
        choices = Tipos_de_licencias.choices,
        default = Tipos_de_licencias.LICENCIA_PARA_CARRO
    )