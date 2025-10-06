from django.db import models

# Para el tipo de licencia, como de moto o carro

class Cat_tipos_de_licencias(models.Model):
    id_tipo_de_licencia = models.AutoField(primary_key=True)
    tipo_de_licencia = models.CharField(max_length=30, unique=True)