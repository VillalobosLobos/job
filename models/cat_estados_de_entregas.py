from django.db import models

#Para saber si la entrega esta: pendiente, terminada o reagendada

class Cat_estados_de_entregas(models.Model):
    id_estado_de_entrega = models.AutoField(primary_key=True)
    estado_de_entrega = models.CharField(max_length=10, unique=True)