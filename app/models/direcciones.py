from django.core.validators import RegexValidator #Para usar expresiones regulares
from .clientes import Clientes
from django.db import models


'''
Tenemos la relación cliente, donde si se elimina un cliente 
la dirección se elimina de la misma manera
'''

class Direcciones(models.Model):
    id = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Clientes, on_delete = models.CASCADE)
    calle = models.TextField()
    numero_exterior = models.CharField(max_length = 20)
    numero_interior = models.CharField(max_length = 20, blank = True, null = True) #opcional
    colonia = models.TextField()
    delegacion = models.TextField()
    cp = models.CharField(
        max_length = 5, 
        validators = [RegexValidator(r'^\d{5}$', message="Código postal inválido")]
    )
    pais = models.CharField(max_length = 70, default = "México")