# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CatEstadosEntrega(models.Model):
    id_estado_entrega = models.AutoField(primary_key=True, db_comment='Identificador único del estado de entrega')
    nombre = models.TextField(unique=True, db_comment='Nombre del estado de entrega (pendiente, entregada)')

    class Meta:
        managed = False
        db_table = 'cat_estados_entrega'
        db_table_comment = 'Catálogo de estados de entrega'


class CatEstatusVehiculo(models.Model):
    id_estatus_vehiculo = models.AutoField(primary_key=True, db_comment='Identificador único del estatus')
    nombre = models.TextField(unique=True, db_comment='Nombre del estatus (libre, ocupado)')

    class Meta:
        managed = False
        db_table = 'cat_estatus_vehiculo'
        db_table_comment = 'Catálogo de estados de los vehículos'


class CatTiposEntrega(models.Model):
    id_tipo_entrega = models.AutoField(primary_key=True, db_comment='Identificador único del tipo de entrega')
    nombre = models.TextField(unique=True, db_comment='Nombre del tipo de entrega (campo, masivo)')

    class Meta:
        managed = False
        db_table = 'cat_tipos_entrega'
        db_table_comment = 'Catálogo de tipos de entrega'


class CatTiposLicencia(models.Model):
    id_tipo_licencia = models.AutoField(primary_key=True, db_comment='Identificador único del tipo de licencia')
    nombre = models.TextField(unique=True, db_comment='Nombre del tipo de licencia (moto, carro, etc.)')

    class Meta:
        managed = False
        db_table = 'cat_tipos_licencia'
        db_table_comment = 'Catálogo de tipos de licencias de repartidor'


class CatTiposVehiculo(models.Model):
    id_tipo_vehiculo = models.AutoField(primary_key=True, db_comment='Identificador único del tipo de vehículo')
    nombre = models.TextField(unique=True, db_comment='Nombre del tipo de vehículo (moto, carro, etc.)')

    class Meta:
        managed = False
        db_table = 'cat_tipos_vehiculo'
        db_table_comment = 'Catálogo de tipos de vehículos'


class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True, db_comment='Identificador único del cliente')
    nombre = models.TextField(db_comment='Nombre completo del cliente')
    telefono = models.TextField(db_comment='Número de teléfono del cliente')

    class Meta:
        managed = False
        db_table = 'clientes'
        db_table_comment = 'Tabla de clientes'


class Direcciones(models.Model):
    id_direccion = models.AutoField(primary_key=True, db_comment='Identificador único de la dirección')
    id_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cliente', db_comment='Referencia al cliente dueño de la dirección')
    calle = models.TextField(db_comment='Nombre de la calle')
    num_ext = models.TextField(db_comment='Número exterior')
    num_int = models.TextField(blank=True, null=True, db_comment='Número interior (opcional)')
    colonia = models.TextField(db_comment='Nombre de la colonia')
    delegacion_municipio = models.TextField(db_comment='Delegación o municipio')
    cp = models.TextField(db_comment='Código postal')
    pais = models.TextField(db_comment='País, por defecto México')

    class Meta:
        managed = False
        db_table = 'direcciones'
        db_table_comment = 'Tabla de direcciones de clientes'


class Entregas(models.Model):
    id_entrega = models.AutoField(primary_key=True, db_comment='Identificador único de la entrega')
    id_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cliente', db_comment='Referencia al cliente')
    id_direccion = models.ForeignKey(Direcciones, models.DO_NOTHING, db_column='id_direccion', db_comment='Referencia a la dirección de entrega')
    id_repartidor_asignado = models.ForeignKey('Repartidores', models.DO_NOTHING, db_column='id_repartidor_asignado', blank=True, null=True, db_comment='Repartidor asignado')
    id_vehiculo_asignado = models.ForeignKey('Vehiculos', models.DO_NOTHING, db_column='id_vehiculo_asignado', blank=True, null=True, db_comment='Vehículo asignado')
    id_tipo_entrega = models.ForeignKey(CatTiposEntrega, models.DO_NOTHING, db_column='id_tipo_entrega', db_comment='Tipo de entrega')
    id_estado_entrega = models.ForeignKey(CatEstadosEntrega, models.DO_NOTHING, db_column='id_estado_entrega', db_comment='Estado actual de la entrega')
    beneficios = models.TextField(blank=True, null=True, db_comment='Son los beneficios que se le entregaran al cliente')
    monto_beneficio = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Será el costo de los beneficios')

    class Meta:
        managed = False
        db_table = 'entregas'
        db_table_comment = 'Tabla de entregas programadas'


class LicenciasRepartidor(models.Model):
    id_licencia = models.AutoField(primary_key=True, db_comment='Identificador único de la licencia')
    id_repartidor = models.ForeignKey('Repartidores', models.DO_NOTHING, db_column='id_repartidor', db_comment='Referencia al repartidor')
    id_tipo_licencia = models.ForeignKey(CatTiposLicencia, models.DO_NOTHING, db_column='id_tipo_licencia', db_comment='Referencia al tipo de licencia')

    class Meta:
        managed = False
        db_table = 'licencias_repartidor'
        db_table_comment = 'Licencias que posee cada repartidor'


class Repartidores(models.Model):
    id_repartidor = models.AutoField(primary_key=True, db_comment='Identificador único del repartidor')
    nombre = models.TextField(db_comment='Nombre completo del repartidor')
    telefono = models.TextField(db_comment='Número de teléfono del repartidor')
    activo = models.BooleanField(blank=True, null=True, db_comment='Indica si el repartidor está activo')

    class Meta:
        managed = False
        db_table = 'repartidores'
        db_table_comment = 'Tabla de repartidores'


class Vehiculos(models.Model):
    id_vehiculo = models.AutoField(primary_key=True, db_comment='Identificador único del vehículo')
    id_tipo_vehiculo = models.ForeignKey(CatTiposVehiculo, models.DO_NOTHING, db_column='id_tipo_vehiculo', db_comment='Referencia al tipo de vehículo')
    modelo = models.TextField(db_comment='Modelo del vehículo')
    km_por_litro = models.DecimalField(max_digits=65535, decimal_places=65535, db_comment='Rendimiento en kilómetros por litro')
    id_estatus_vehiculo = models.ForeignKey(CatEstatusVehiculo, models.DO_NOTHING, db_column='id_estatus_vehiculo', db_comment='Estado actual del vehículo')
    id_repartidor_actual = models.ForeignKey(Repartidores, models.DO_NOTHING, db_column='id_repartidor_actual', blank=True, null=True, db_comment='Repartidor que actualmente usa el vehículo')

    class Meta:
        managed = False
        db_table = 'vehiculos'
        db_table_comment = 'Tabla de vehículos disponibles'
