from .estatus_de_vehiculos import Estatus_de_vehiculos
from .tipos_de_vehiculos import Tipos_de_vehiculos
from django.core.validators import MinValueValidator
from .repartidores import Repartidores
from django.db import models

'''
Tenemos la clase Vehiculos donde tendremo un id, hacemos referencia a el tipo
de vehiculo que es, modelo, kilometro recorrido por litro, estatus del vehiculo
y además un repartidor
'''

class Vehiculos(models.Model):
    id = models.AutoField(primary_key = True)
    tipo_de_vehiculo = models.CharField(
        max_length = 10,
        choices = Tipos_de_vehiculos.choices,
        default = Tipos_de_vehiculos.CARRO
    )
    modelo = models.TextField()
    km_por_litro = models.IntegerField(validators=[MinValueValidator(1)]) #Para no aceptar valores negativos
    estatus_vehiculo = models.CharField(
        max_length = 10,
        choices = Estatus_de_vehiculos.choices,
        default = Estatus_de_vehiculos.LIBRE
    )
    id_repartidor = models.ForeignKey(
        Repartidores, 
        on_delete = models.SET_NULL, #si se elimina el repartidor que no se elimine el vehiculo, solo salga como NULL
        blank = True,
        null = True
    )