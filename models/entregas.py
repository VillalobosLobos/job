
from .cat_estados_de_entregas import Cat_estados_de_entregas
from .cat_tipos_de_entregas import Cat_tipos_de_entregas
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
    id_entrega = models.AutoField(primary_key = True)
    cliente = models.ForeignKey(Clientes, on_delete = models.CASCADE)
    direccion = models.ForeignKey(Direcciones, on_delete = models.CASCADE)
    repartidor = models.ForeignKey(Repartidores, on_delete = models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculos, on_delete = models.CASCADE)
    tipo_de_entrega = models.ForeignKey(Cat_tipos_de_entregas, on_delete = models.CASCADE)
    estado_de_la_entrega = models.ForeignKey(
        Cat_estados_de_entregas,
        on_delete = models.CASCADE
    )
    beneficios = models.TextField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

