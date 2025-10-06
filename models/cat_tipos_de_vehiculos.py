from django.db import models

# Para poner el tipo de vehiculo, como carro, moto, camión de carga, etc...

class Cat_tipos_de_vehiculos(models.Model):
    id_tipo_de_vehiculo = models.AutoField(primary_key=True)
    tipo_de_vehiculo = models.CharField(max_length=50, unique=True)