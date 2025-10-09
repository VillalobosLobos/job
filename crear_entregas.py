from app.models import Clientes, Direcciones, Entregas, Repartidores, Vehiculos, Estados_de_entregas
import random

# 🔹 Eliminar entregas, direcciones y clientes anteriores
Entregas.objects.all().delete()
Direcciones.objects.all().delete()
Clientes.objects.all().delete()
print("🧹 Entregas, direcciones y clientes eliminados.")

# 🔹 Crear o recuperar repartidor
repartidor, _ = Repartidores.objects.get_or_create(
    telefono="5523456789",
    defaults={"nombre": "Luis Gómez", "activo": True}
)

# 🔹 Crear o recuperar vehículo (toma el primero libre del repartidor)
vehiculo = Vehiculos.objects.filter(id_repartidor=repartidor, estatus_vehiculo="libre").first()
if not vehiculo:
    vehiculo = Vehiculos.objects.create(
        tipo_de_vehiculo="carro",
        modelo="Nissan Versa",
        km_por_litro=15,
        estatus_vehiculo="libre",
        id_repartidor=repartidor
    )

# 🔹 Función auxiliar para cliente + dirección
def crear_cliente_direccion(nombre, telefono, calle, ext, int_, colonia, delegacion, cp):
    cliente = Clientes.objects.filter(telefono=telefono).first()
    if not cliente:
        cliente = Clientes.objects.create(nombre=nombre, telefono=telefono)
    else:
        cliente.nombre = nombre  # actualiza nombre si cambió
        cliente.save()

    direccion = Direcciones.objects.filter(id_cliente=cliente).first()
    if not direccion:
        direccion = Direcciones.objects.create(
            id_cliente=cliente,
            calle=calle,
            numero_exterior=ext,
            numero_interior=int_,
            colonia=colonia,
            delegacion=delegacion,
            cp=cp
        )
    return cliente, direccion

# 🔹 Direcciones reales
direcciones_reales = [
    ("Río Volga", "55", "", "Cuauhtémoc", "Cuauhtémoc", "06500"),
    ("C. Río Lerma", "113", "", "Cuauhtémoc", "Cuauhtémoc", "06500"),
    ("C. Jose Rosas Moreno", "69", "", "San Rafael", "Cuauhtémoc", "06470"),
    ("Tomas a Edison", "69", "", "Tabacalera", "Cuauhtémoc", "06030"),
    ("San Ildefonso", "30", "", "Centro Histórico", "Cuauhtémoc", "06020"),
    ("Lope de Vega", "406", "", "Polanco V Secc", "Miguel Hidalgo", "11560"),
    ("Ángel del Campo", "10-1", "", "Obrera", "Cuauhtémoc", "06720"),
    ("Francisco Olaguibel", "75BIS", "", "Obrera", "Cuauhtémoc", "06800"),
]

# 🔹 Crear entregas pendientes
for i in range(3):
    nombre = f"Cliente Pendiente {i+1}"
    telefono = f"55123456{80+i}"
    calle, ext, int_, colonia, delegacion, cp = direcciones_reales[i]
    cliente, direccion = crear_cliente_direccion(nombre, telefono, calle, ext, int_, colonia, delegacion, cp)

    entrega = Entregas.objects.create(
        id_cliente=cliente,
        id_direccion=direccion,
        id_repartidor=repartidor,
        id_vehiculo=vehiculo,
        tipo_de_entrega=random.choice(["campo", "masivo"]),
        estado_de_la_entrega=Estados_de_entregas.PENDIENTE,
        beneficios=f"Entrega pendiente {i+1}",
        monto=random.randint(100, 300)
    )
    print(f"✅ Entrega pendiente {i+1} creada → ID {entrega.id}")

# 🔹 Crear entregas terminadas
for i in range(3):
    nombre = f"Cliente Terminado {i+1}"
    telefono = f"55123456{90+i}"
    calle, ext, int_, colonia, delegacion, cp = direcciones_reales[i+3]
    cliente, direccion = crear_cliente_direccion(nombre, telefono, calle, ext, int_, colonia, delegacion, cp)

    entrega = Entregas.objects.create(
        id_cliente=cliente,
        id_direccion=direccion,
        id_repartidor=repartidor,
        id_vehiculo=vehiculo,
        tipo_de_entrega=random.choice(["campo", "masivo"]),
        estado_de_la_entrega=Estados_de_entregas.TERMINADA,
        beneficios=f"Entrega terminada {i+1}",
        monto=random.randint(300, 500)
    )
    print(f"✅ Entrega terminada {i+1} creada → ID {entrega.id}")

# 🔹 Crear entregas reagendadas
for i in range(2):  # Solo quedan 2 direcciones
    nombre = f"Cliente Reagendado {i+1}"
    telefono = f"55123456{70+i}"
    calle, ext, int_, colonia, delegacion, cp = direcciones_reales[i+6]
    cliente, direccion = crear_cliente_direccion(nombre, telefono, calle, ext, int_, colonia, delegacion, cp)

    entrega = Entregas.objects.create(
        id_cliente=cliente,
        id_direccion=direccion,
        id_repartidor=repartidor,
        id_vehiculo=vehiculo,
        tipo_de_entrega=random.choice(["campo", "masivo"]),
        estado_de_la_entrega=Estados_de_entregas.REAGENDADA,
        beneficios=f"Entrega reagendada {i+1}",
        monto=random.randint(150, 400)
    )
    print(f"✅ Entrega reagendada {i+1} creada → ID {entrega.id}")
