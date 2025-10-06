from django.db import models

#Para definir los tipos de entrega como: campo, masivo, etc...

class Cat_tipos_de_entregas(models.Model):
    id_tipo_de_entrega = models.AutoField(primary_key=True)
    tipo_de_entrega = models.CharField(max_length=8, unique=True)

