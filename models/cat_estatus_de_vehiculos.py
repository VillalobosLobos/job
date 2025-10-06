from django.db import models

#Para marcar cuando un vehiculo está : ocupado , libre, etc.

class Cat_estatus_de_vehiculos(models.Model):
    id_estatus_de_vehiculo = models.AutoField(primary_key= True)
    estatus_de_vehiculo = models.CharField(max_length=15, unique=True)