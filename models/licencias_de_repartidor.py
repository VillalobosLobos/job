from .cat_tipos_de_licencias import Cat_tipos_de_licencias
from .repartidores import Repartidores
from django.db import models

'''
Se hace referencia a el repatidor y al tipo de licencia,
donde si se elimina el repartidor o tipos de licencia se
eliminan las licencias
'''

class Licencias_de_repartidor(models.Model):
    id_licencia_de_repartidor = models.AutoField(primary_key = True)
    repartidor = models.ForeignKey(Repartidores, on_delete = models.CASCADE)
    tipo_de_licencia = models.ForeignKey(Cat_tipos_de_licencias, on_delete = models.CASCADE)