import sqlite3
import os

_dir = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(_dir, 'taller.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()

    c.executescript('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            direccion TEXT,
            telefono TEXT,
            email TEXT,
            dni TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS vehiculos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            marca TEXT NOT NULL,
            modelo TEXT NOT NULL,
            patente TEXT NOT NULL UNIQUE,
            anio INTEGER,
            motor TEXT,
            vin TEXT,
            color TEXT,
            combustible TEXT,
            cliente_id INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        );

        CREATE TABLE IF NOT EXISTS ordenes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehiculo_id INTEGER NOT NULL,
            cliente_id INTEGER NOT NULL,
            fecha_ingreso DATE NOT NULL,
            fecha_estimada DATE,
            fecha_egreso DATE,
            kilometros INTEGER,
            receptor_servicio TEXT,
            descripcion_trabajo TEXT,
            diagnostico TEXT,
            repuestos TEXT,
            observaciones TEXT,
            estado TEXT DEFAULT 'abierta',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (vehiculo_id) REFERENCES vehiculos(id),
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        );

        CREATE TABLE IF NOT EXISTS presupuestos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            vehiculo_id INTEGER,
            fecha DATE NOT NULL,
            valido_hasta DATE,
            descripcion TEXT,
            observaciones TEXT,
            atendido_por TEXT,
            condicion_venta TEXT,
            estado TEXT DEFAULT 'pendiente',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id),
            FOREIGN KEY (vehiculo_id) REFERENCES vehiculos(id)
        );

        CREATE TABLE IF NOT EXISTS presupuesto_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            presupuesto_id INTEGER NOT NULL,
            tipo TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            cantidad REAL DEFAULT 1,
            precio_unitario REAL DEFAULT 0,
            en_stock INTEGER DEFAULT 0,
            FOREIGN KEY (presupuesto_id) REFERENCES presupuestos(id)
        );
    ''')
    conn.commit()
    conn.close()
