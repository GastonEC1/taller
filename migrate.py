"""
Ejecutar UNA SOLA VEZ para agregar los campos nuevos a la base de datos existente.
Uso: python migrate.py
"""
import sqlite3, os

_dir = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(_dir, 'taller.db')

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

migraciones = [
    # Clientes
    ("ALTER TABLE clientes ADD COLUMN email TEXT",         "clientes.email"),
    ("ALTER TABLE clientes ADD COLUMN dni TEXT",           "clientes.dni"),
    # Vehículos
    ("ALTER TABLE vehiculos ADD COLUMN vin TEXT",          "vehiculos.vin"),
    ("ALTER TABLE vehiculos ADD COLUMN color TEXT",        "vehiculos.color"),
    ("ALTER TABLE vehiculos ADD COLUMN combustible TEXT",  "vehiculos.combustible"),
    # Órdenes
    ("ALTER TABLE ordenes ADD COLUMN fecha_estimada DATE", "ordenes.fecha_estimada"),
    ("ALTER TABLE ordenes ADD COLUMN receptor_servicio TEXT", "ordenes.receptor_servicio"),
    ("ALTER TABLE ordenes ADD COLUMN observaciones TEXT",  "ordenes.observaciones"),
    # Presupuestos
    ("ALTER TABLE presupuestos ADD COLUMN condicion_venta TEXT", "presupuestos.condicion_venta"),
    # Ítems presupuesto
    ("ALTER TABLE presupuesto_items ADD COLUMN en_stock INTEGER DEFAULT 0", "presupuesto_items.en_stock"),
]

for sql, nombre in migraciones:
    try:
        c.execute(sql)
        print(f"  ✓ {nombre}")
    except sqlite3.OperationalError as e:
        if "duplicate column" in str(e):
            print(f"  – {nombre} (ya existía)")
        else:
            print(f"  ✗ {nombre}: {e}")

conn.commit()
conn.close()
print("\nMigración completada.")
