from django.core.validators import RegexValidator #Para usar expresiones regulares
from django.db import models

'''
El campo de activo hace referencia a si el repartidor está disponible
disponible = True
ocupado = False
'''

class Repartidores(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.TextField()
    telefono = models.CharField(
        max_length =15,
        unique = True,
        validators = [RegexValidator(r'^\+?\d{10,13}$', message="Número de teléfono inválido")]
    )
    activo = models.BooleanField()