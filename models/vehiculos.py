from .cat_estatus_de_vehiculos import Cat_estatus_de_vehiculos
from .cat_tipos_de_vehiculos import Cat_tipos_de_vehiculos
from django.core.validators import MinValueValidator
from .repartidores import Repartidores
from django.db import models

'''
Tenemos la clase Vehiculos donde tendremo un id, hacemos referencia a el tipo
de vehiculo que es, modelo, kilometro recorrido por litro, estatus del vehiculo
y además un repartidor
'''

class Vehiculos(models.Model):
    id_vehiculo = models.AutoField(primary_key = True)
    tipo_de_vehiculo = models.ForeignKey(Cat_tipos_de_vehiculos, on_delete = models.CASCADE)
    modelo = models.TextField()
    km_por_litro = models.IntegerField(validators=[MinValueValidator(1)]) #Para no aceptar valores negativos
    estatus_vehiculo = models.ForeignKey(Cat_estatus_de_vehiculos, on_delete = models.CASCADE)
    repartidor = models.ForeignKey(
        Repartidores, 
        on_delete = models.SET_NULL, #si se elimina el repartidor que no se elimine el vehiculo, solo salga como NULL
        blank = True,
        null = True
    )