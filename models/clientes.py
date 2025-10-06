from django.core.validators import RegexValidator #Para usar expresiones regulares
from django.db import models

'''
Tenemos la tabla para nuestros cliente,
se usa una expresión regular para números "válidos", como:
5512345678
+525512345678

y que sea único por cliente
'''

class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.TextField()
    telefono = models.CharField(
        max_length =15,
        unique = True,
        validators = [RegexValidator(r'^\+?\d{10,13}$', message="Número de teléfono inválido")]
    )