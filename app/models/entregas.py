
from .estados_de_entregas import Estados_de_entregas
from .tipos_de_entregas import Tipos_de_entregas
from .repartidores import Repartidores
from .direcciones import Direcciones
from .vehiculos import Vehiculos
from .clientes import Clientes
from django.db import models

'''
La clase entregas es donde se crearan las entregas para repartir, todas tienen el método
CASCADE para evitar datos huerfanos o problemas de relaciones
'''

class Entregas(models.Model):
    id = models.AutoField(primary_key = True)
    id_cliente = models.ForeignKey(Clientes, on_delete = models.CASCADE)
    id_direccion = models.ForeignKey(Direcciones, on_delete = models.CASCADE)
    id_repartidor = models.ForeignKey(Repartidores, on_delete = models.SET_NULL, blank = True, null = True)
    id_vehiculo = models.ForeignKey(Vehiculos, on_delete = models.SET_NULL, blank = True, null = True)
    tipo_de_entrega = models.CharField(
        max_length = 10,
        choices = Tipos_de_entregas.choices,
        default = Tipos_de_entregas.CAMPO
    )
    estado_de_la_entrega = models.CharField(
        max_length = 15,
        choices = Estados_de_entregas.choices,
        default = Estados_de_entregas.REAGENDADA
    )
    beneficios = models.TextField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

