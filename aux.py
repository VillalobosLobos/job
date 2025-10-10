from app.models import Repartidores, Vehiculos, Licencias_de_repartidor
from app.models.estatus_de_vehiculos import Estatus_de_vehiculos
from app.models.tipos_de_licencias import Tipos_de_licencias
from app.models.tipos_de_vehiculos import Tipos_de_vehiculos

# 🔥 Eliminar todo
Licencias_de_repartidor.objects.all().delete()
Vehiculos.objects.all().delete()
Repartidores.objects.all().delete()

# ✅ Crear repartidores disponibles
repartidores_data = [
    {"nombre": "Luis Martínez", "telefono": "+525512345678"},
    {"nombre": "Juan Martínez", "telefono": "+525592345678"},
    {"nombre": "Pablo Martínez", "telefono": "+525512335978"},
    {"nombre": "Luis Gómez", "telefono": "5523456789"},
]

repartidores_creados = []
for data in repartidores_data:
    repartidor = Repartidores.objects.create(
        nombre=data["nombre"],
        telefono=data["telefono"],
        activo=True
    )
    repartidores_creados.append(repartidor)

    # Asignar licencia por defecto
    Licencias_de_repartidor.objects.create(
        id_repartidor=repartidor,
        tipo_de_licencia=Tipos_de_licencias.LICENCIA_PARA_CARRO
    )

# 🚗 Crear vehículos disponibles (sin asignar a ningún repartidor)
vehiculos_data = [
    {"modelo": "Nissan Versa", "tipo": Tipos_de_vehiculos.CARRO, "km_por_litro": 14},
    {"modelo": "Honda Civic", "tipo": Tipos_de_vehiculos.CARRO, "km_por_litro": 15},
    {"modelo": "Toyota Hilux", "tipo": Tipos_de_vehiculos.CARRO, "km_por_litro": 12},
    {"modelo": "Chevrolet Aveo", "tipo": Tipos_de_vehiculos.CARRO, "km_por_litro": 13},
    {"modelo": "Renault Kwid", "tipo": Tipos_de_vehiculos.CARRO, "km_por_litro": 16},
]

for data in vehiculos_data:
    Vehiculos.objects.create(
        modelo=data["modelo"],
        tipo_de_vehiculo=data["tipo"],
        km_por_litro=data["km_por_litro"],
        estatus_vehiculo=Estatus_de_vehiculos.LIBRE,
        id_repartidor=None
    )

print("✅ Repartidores, licencias y vehículos creados correctamente.")
