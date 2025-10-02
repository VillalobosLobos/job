-- =============================================
-- BASE DE DATOS DELIVERY
-- =============================================

-- =============================================
-- LIMPIEZA DE TABLAS EXISTENTES
-- =============================================
DROP TABLE IF EXISTS entregas CASCADE;
DROP TABLE IF EXISTS vehiculos CASCADE;
DROP TABLE IF EXISTS licencias_repartidor CASCADE;
DROP TABLE IF EXISTS repartidores CASCADE;
DROP TABLE IF EXISTS direcciones CASCADE;
DROP TABLE IF EXISTS clientes CASCADE;

DROP TABLE IF EXISTS cat_estados_entrega CASCADE;
DROP TABLE IF EXISTS cat_tipos_entrega CASCADE;
DROP TABLE IF EXISTS cat_estatus_vehiculo CASCADE;
DROP TABLE IF EXISTS cat_tipos_vehiculo CASCADE;
DROP TABLE IF EXISTS cat_tipos_licencia CASCADE;

-- =============================================
-- CATÁLOGOS
-- =============================================
CREATE TABLE cat_tipos_licencia (
    id_tipo_licencia SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL UNIQUE
);
--INSERT INTO cat_tipos_licencia (nombre) VALUES ('moto'), ('carro');

CREATE TABLE cat_tipos_vehiculo (
    id_tipo_vehiculo SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL UNIQUE
);
--INSERT INTO cat_tipos_vehiculo (nombre) VALUES ('moto'), ('carro');

CREATE TABLE cat_estatus_vehiculo (
    id_estatus_vehiculo SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL UNIQUE
);
--INSERT INTO cat_estatus_vehiculo (nombre) VALUES ('libre'), ('ocupado');

CREATE TABLE cat_tipos_entrega (
    id_tipo_entrega SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL UNIQUE
);
--INSERT INTO cat_tipos_entrega (nombre) VALUES ('campo'), ('masivo');

CREATE TABLE cat_estados_entrega (
    id_estado_entrega SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL UNIQUE
);
--INSERT INTO cat_estados_entrega (nombre) VALUES ('pendiente'), ('entregada'), ('reagendar');

-- =============================================
-- TABLAS PRINCIPALES
-- =============================================
CREATE TABLE clientes (
    id_cliente SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    telefono TEXT NOT NULL
);

CREATE TABLE direcciones (
    id_direccion SERIAL PRIMARY KEY,
    id_cliente INT NOT NULL REFERENCES clientes(id_cliente) ON DELETE CASCADE,
    calle TEXT NOT NULL,
    num_ext TEXT NOT NULL,
    num_int TEXT,
    colonia TEXT NOT NULL,
    delegacion_municipio TEXT NOT NULL,
    cp TEXT NOT NULL,
    pais TEXT NOT NULL DEFAULT 'México'
);

CREATE TABLE repartidores (
    id_repartidor SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    telefono TEXT NOT NULL,
    activo BOOLEAN DEFAULT TRUE
);

CREATE TABLE licencias_repartidor (
    id_licencia SERIAL PRIMARY KEY,
    id_repartidor INT NOT NULL REFERENCES repartidores(id_repartidor) ON DELETE CASCADE,
    id_tipo_licencia INT NOT NULL REFERENCES cat_tipos_licencia(id_tipo_licencia)
);

CREATE TABLE vehiculos (
    id_vehiculo SERIAL PRIMARY KEY,
    id_tipo_vehiculo INT NOT NULL REFERENCES cat_tipos_vehiculo(id_tipo_vehiculo),
    modelo TEXT NOT NULL,
    km_por_litro NUMERIC NOT NULL,
    id_estatus_vehiculo INT NOT NULL REFERENCES cat_estatus_vehiculo(id_estatus_vehiculo) DEFAULT 1,
    id_repartidor_actual INT REFERENCES repartidores(id_repartidor)
);

CREATE TABLE entregas (
    id_entrega SERIAL PRIMARY KEY,
    id_cliente INT NOT NULL REFERENCES clientes(id_cliente) ON DELETE CASCADE,
    id_direccion INT NOT NULL REFERENCES direcciones(id_direccion),
    id_repartidor_asignado INT REFERENCES repartidores(id_repartidor),
    id_vehiculo_asignado INT REFERENCES vehiculos(id_vehiculo),
    id_tipo_entrega INT NOT NULL REFERENCES cat_tipos_entrega(id_tipo_entrega),
    id_estado_entrega INT NOT NULL REFERENCES cat_estados_entrega(id_estado_entrega) DEFAULT 1,
    beneficios TEXT,
    monto_beneficio NUMERIC
);

-- =============================================
-- COMENTARIOS
-- =============================================
COMMENT ON TABLE cat_tipos_licencia IS 'Catálogo de tipos de licencias de repartidor';
COMMENT ON COLUMN cat_tipos_licencia.id_tipo_licencia IS 'Identificador único del tipo de licencia';
COMMENT ON COLUMN cat_tipos_licencia.nombre IS 'Nombre del tipo de licencia (moto, carro, etc.)';

COMMENT ON TABLE cat_tipos_vehiculo IS 'Catálogo de tipos de vehículos';
COMMENT ON COLUMN cat_tipos_vehiculo.id_tipo_vehiculo IS 'Identificador único del tipo de vehículo';
COMMENT ON COLUMN cat_tipos_vehiculo.nombre IS 'Nombre del tipo de vehículo (moto, carro, etc.)';

COMMENT ON TABLE cat_estatus_vehiculo IS 'Catálogo de estados de los vehículos';
COMMENT ON COLUMN cat_estatus_vehiculo.id_estatus_vehiculo IS 'Identificador único del estatus';
COMMENT ON COLUMN cat_estatus_vehiculo.nombre IS 'Nombre del estatus (libre, ocupado)';

COMMENT ON TABLE cat_tipos_entrega IS 'Catálogo de tipos de entrega';
COMMENT ON COLUMN cat_tipos_entrega.id_tipo_entrega IS 'Identificador único del tipo de entrega';
COMMENT ON COLUMN cat_tipos_entrega.nombre IS 'Nombre del tipo de entrega (campo, masivo)';

COMMENT ON TABLE cat_estados_entrega IS 'Catálogo de estados de entrega';
COMMENT ON COLUMN cat_estados_entrega.id_estado_entrega IS 'Identificador único del estado de entrega';
COMMENT ON COLUMN cat_estados_entrega.nombre IS 'Nombre del estado de entrega (pendiente, entregada)';

COMMENT ON TABLE clientes IS 'Tabla de clientes';
COMMENT ON COLUMN clientes.id_cliente IS 'Identificador único del cliente';
COMMENT ON COLUMN clientes.nombre IS 'Nombre completo del cliente';
COMMENT ON COLUMN clientes.telefono IS 'Número de teléfono del cliente';

COMMENT ON TABLE direcciones IS 'Tabla de direcciones de clientes';
COMMENT ON COLUMN direcciones.id_direccion IS 'Identificador único de la dirección';
COMMENT ON COLUMN direcciones.id_cliente IS 'Referencia al cliente dueño de la dirección';
COMMENT ON COLUMN direcciones.calle IS 'Nombre de la calle';
COMMENT ON COLUMN direcciones.num_ext IS 'Número exterior';
COMMENT ON COLUMN direcciones.num_int IS 'Número interior (opcional)';
COMMENT ON COLUMN direcciones.colonia IS 'Nombre de la colonia';
COMMENT ON COLUMN direcciones.delegacion_municipio IS 'Delegación o municipio';
COMMENT ON COLUMN direcciones.cp IS 'Código postal';
COMMENT ON COLUMN direcciones.pais IS 'País, por defecto México';

COMMENT ON TABLE repartidores IS 'Tabla de repartidores';
COMMENT ON COLUMN repartidores.id_repartidor IS 'Identificador único del repartidor';
COMMENT ON COLUMN repartidores.nombre IS 'Nombre completo del repartidor';
COMMENT ON COLUMN repartidores.telefono IS 'Número de teléfono del repartidor';
COMMENT ON COLUMN repartidores.activo IS 'Indica si el repartidor está activo';

COMMENT ON TABLE licencias_repartidor IS 'Licencias que posee cada repartidor';
COMMENT ON COLUMN licencias_repartidor.id_licencia IS 'Identificador único de la licencia';
COMMENT ON COLUMN licencias_repartidor.id_repartidor IS 'Referencia al repartidor';
COMMENT ON COLUMN licencias_repartidor.id_tipo_licencia IS 'Referencia al tipo de licencia';

COMMENT ON TABLE vehiculos IS 'Tabla de vehículos disponibles';
COMMENT ON COLUMN vehiculos.id_vehiculo IS 'Identificador único del vehículo';
COMMENT ON COLUMN vehiculos.id_tipo_vehiculo IS 'Referencia al tipo de vehículo';
COMMENT ON COLUMN vehiculos.modelo IS 'Modelo del vehículo';
COMMENT ON COLUMN vehiculos.km_por_litro IS 'Rendimiento en kilómetros por litro';
COMMENT ON COLUMN vehiculos.id_estatus_vehiculo IS 'Estado actual del vehículo';
COMMENT ON COLUMN vehiculos.id_repartidor_actual IS 'Repartidor que actualmente usa el vehículo';

COMMENT ON TABLE entregas IS 'Tabla de entregas programadas';
COMMENT ON COLUMN entregas.id_entrega IS 'Identificador único de la entrega';
COMMENT ON COLUMN entregas.id_cliente IS 'Referencia al cliente';
COMMENT ON COLUMN entregas.id_direccion IS 'Referencia a la dirección de entrega';
COMMENT ON COLUMN entregas.id_repartidor_asignado IS 'Repartidor asignado';
COMMENT ON COLUMN entregas.id_vehiculo_asignado IS 'Vehículo asignado';
COMMENT ON COLUMN entregas.id_tipo_entrega IS 'Tipo de entrega';
COMMENT ON COLUMN entregas.id_estado_entrega IS 'Estado actual de la entrega';
COMMENT ON COLUMN entregas.beneficios IS 'Son los beneficios que se le entregaran al cliente';
COMMENT ON COLUMN entregas.monto_beneficio IS 'Será el costo de los beneficios';

-- =============================================
-- Índices SQL
-- =============================================

-- Indices para la tabla de entregas
-- Para saber qué entregas están pendientes o terminadas
DROP INDEX IF EXISTS idx_entregas_estado_tipo;
CREATE INDEX IF NOT EXISTS idx_entregas_estado_tipo ON entregas (id_estado_entrega, id_tipo_entrega);
-- Para saber qué entregas tiene cada repartidor
DROP INDEX IF EXISTS idx_entregas_repartidor;
CREATE INDEX IF NOT EXISTS idx_entregas_repartidor ON entregas (id_repartidor_asignado);


-- Indices para la tabla de vehiculos
-- Para encontrar vehículos libres u ocupados
DROP INDEX IF EXISTS idx_vehiculos_estatus;
CREATE INDEX IF NOT EXISTS idx_vehiculos_estatus ON vehiculos (id_estatus_vehiculo);
-- Para saber qué vehículo está usando cada repartidor
DROP INDEX IF EXISTS idx_vehiculos_repartidor;
CREATE INDEX IF NOT EXISTS idx_vehiculos_repartidor ON vehiculos (id_repartidor_actual);


-- Indices para la tabla repartidores
-- Para filtrar rápido qué repartidor está disponible
DROP INDEX IF EXISTS idx_repartidores_activo;
CREATE INDEX IF NOT EXISTS idx_repartidores_activo ON repartidores (activo);

-- Indices para la tabla de licencias
-- Para saber qué repartidores tienen licencia de moto o carro
DROP INDEX IF EXISTS idx_licencias_tipo;
CREATE INDEX IF NOT EXISTS idx_licencias_tipo ON licencias_repartidor (id_tipo_licencia);

-- Indices para la tabla de direcciones
-- Para obtener rápidamente las direcciones de un cliente
DROP INDEX IF EXISTS idx_direcciones_cliente;
CREATE INDEX IF NOT EXISTS idx_direcciones_cliente ON direcciones (id_cliente);

-- ================================================================================================
--                                      Procesamiento almacenado
-- =================================================================================================

---------------------- Insertar ----------------------------------------------------------
-- Para agregar elementos al catalogo tipo de licencia
CREATE OR REPLACE PROCEDURE insertar_tipo_licencia(
    IN p_nombre TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO cat_tipos_licencia(nombre) VALUES (p_nombre);
END;
$$;

-- Para agregar elementos al catalogo tipo de vehiculo
CREATE OR REPLACE PROCEDURE insertar_tipo_vehiculo(
    IN p_nombre TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO cat_tipos_vehiculo(nombre) VALUES (p_nombre);
END;
$$;

-- Para agregar elementos al catalogo estatus del vehiculo
CREATE OR REPLACE PROCEDURE insertar_estatus_vehiculo(
    IN p_nombre TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO cat_estatus_vehiculo(nombre) VALUES (p_nombre);
END;
$$;

-- Para agregar elementos al catalogo tipo de entrega
CREATE OR REPLACE PROCEDURE insertar_tipo_entrega(
    IN p_nombre TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO cat_tipos_entrega(nombre) VALUES (p_nombre);
END;
$$;

-- Para agregar elementos al catalogo de estado
CREATE OR REPLACE PROCEDURE insertar_estado_entrega(
    IN p_nombre TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO cat_estados_entrega(nombre) VALUES (p_nombre);
END;
$$;

-- insertar cliente
CREATE OR REPLACE PROCEDURE insertar_cliente(
    IN p_nombre_cliente TEXT,
    IN p_telefono_cliente TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO clientes (nombre, telefono) VALUES (p_nombre_cliente, p_telefono_cliente);
END;
$$;

-- insertar direccion
CREATE OR REPLACE PROCEDURE insertar_direccion(
    IN cliente_id INT,
    IN p_calle TEXT,
    IN p_num_ext TEXT,
    IN p_num_int TEXT,
    IN p_colonia TEXT,
    IN p_municipio TEXT,
    IN p_cp TEXT,
    IN p_pais TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO direcciones (
        id_cliente, calle, num_ext, num_int, colonia, delegacion_municipio, cp, pais
    ) VALUES (
        cliente_id, p_calle, p_num_ext, p_num_int, p_colonia, p_municipio, p_cp, p_pais
    );
END;
$$;

-- insetar entrega
CREATE OR REPLACE PROCEDURE insertar_entrega(
    IN cliente_id INT,
    IN direccion_id INT,
    IN p_id_tipo_entrega INT,
    IN p_beneficio TEXT,
    IN p_monto NUMERIC
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO entregas (
        id_cliente, id_direccion, id_tipo_entrega, id_estado_entrega,
        beneficios, monto_beneficio
    ) VALUES (
        cliente_id, direccion_id, p_id_tipo_entrega, 3,
        p_beneficio, p_monto
    );
END;
$$;

-- insertar repartidor
CREATE OR REPLACE PROCEDURE insertar_repartidor(
    IN p_nombre TEXT,
    IN p_telefono TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO repartidores (nombre, telefono, activo)
    VALUES (p_nombre, p_telefono, TRUE);
END;
$$;

-- Para insertar la licencia a un repartidore
CREATE OR REPLACE PROCEDURE insertar_licencia_a_repartidor(
    IN p_id_repartidor INT,
    IN p_id_tipo_licencia INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO licencias_repartidor (id_repartidor, id_tipo_licencia)
    VALUES (p_id_repartidor, p_id_tipo_licencia);
END;
$$;

-- Para insertar un vehiculo
CREATE OR REPLACE PROCEDURE insertar_vehiculo(
    IN p_id_tipo_vehiculo INT,
    IN p_modelo TEXT,
    IN p_km_por_litro NUMERIC,
    IN p_id_estatus_vehiculo INT,
    IN p_id_repartidor_actual INT DEFAULT NULL
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO vehiculos (
        id_tipo_vehiculo,
        modelo,
        km_por_litro,
        id_estatus_vehiculo,
        id_repartidor_actual
    )
    VALUES (
        p_id_tipo_vehiculo,
        p_modelo,
        p_km_por_litro,
        p_id_estatus_vehiculo,
        p_id_repartidor_actual
    );
END;
$$;

------------------------------- actualizar ---------------------------------------
-- actualizar cliente
CREATE OR REPLACE PROCEDURE actualizar_cliente(
    IN p_nombre_cliente TEXT,
    IN p_telefono_cliente TEXT,
    IN cliente_id INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE clientes
    SET nombre = p_nombre_cliente,
        telefono = p_telefono_cliente
    WHERE id_cliente = cliente_id;
END;
$$;

-- actualizar direcciones
CREATE OR REPLACE PROCEDURE actualizar_direccion(
    IN p_calle TEXT,
    IN p_num_ext TEXT,
    IN p_num_int TEXT,
    IN p_colonia TEXT,
    IN p_municipio TEXT,
    IN p_cp TEXT,
    IN p_pais TEXT,
    IN direccion_id INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE direcciones
    SET calle = p_calle,
        num_ext = p_num_ext,
        num_int = p_num_int,
        colonia = p_colonia,
        delegacion_municipio = p_municipio,
        cp = p_cp,
        pais = p_pais
    WHERE id_direccion = direccion_id;
END;
$$;

-- actualizar entrega
CREATE OR REPLACE PROCEDURE actualizar_entrega(
    IN p_id_tipo_entrega INT,
    IN p_beneficio TEXT,
    IN p_monto NUMERIC,
    IN p_id_entrega INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE entregas
    SET id_tipo_entrega = p_id_tipo_entrega,
        beneficios = p_beneficio,
        monto_beneficio = p_monto
    WHERE id_entrega = p_id_entrega;
END;
$$;

-- actualizar entrega reagendada a pendiente
CREATE OR REPLACE PROCEDURE actualizar_reagendado_a_pendiente()
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE entregas
    SET id_estado_entrega = 1
    WHERE id_estado_entrega = 3;
END;
$$;

-- Para marcar como terminada la entrega
CREATE OR REPLACE PROCEDURE marcar_entrega_terminada(IN p_id_entrega INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE entregas
    SET id_estado_entrega = 2
    WHERE id_entrega = p_id_entrega;
END;
$$;


-------------------------------------- Eliminar -----------------------------------------------
--- eliminar entrega
CREATE OR REPLACE PROCEDURE eliminar_entrega(
    IN p_id_entrega INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM entregas WHERE id_entrega = p_id_entrega;
END;
$$;

-- eliminar direccion
CREATE OR REPLACE PROCEDURE eliminar_direccion(
    IN direccion_id INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM direcciones WHERE id_direccion = direccion_id;

END;
$$;

-- eliminar cliente
CREATE OR REPLACE PROCEDURE eliminar_cliente(
    IN cliente_id INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM clientes WHERE id_cliente = cliente_id;

END;
$$;

-- ================================================================================================
--                                            Funciones
-- =================================================================================================

-- seleccionar entregas pendientes
DROP FUNCTION IF EXISTS seleccionar_entregas_pendientes();

CREATE OR REPLACE FUNCTION seleccionar_entregas_pendientes()
RETURNS TABLE ( id_entrega INTEGER, cliente TEXT, tipo_entrega TEXT)
LANGUAGE sql 
AS $$
    SELECT e.id_entrega, c.nombre, t.nombre
    FROM entregas e
    JOIN clientes c ON e.id_cliente = c.id_cliente
    JOIN cat_tipos_entrega t ON e.id_tipo_entrega = t.id_tipo_entrega
    WHERE e.id_estado_entrega = 1; -- estado pendiente
$$;

-- seleccionar entregas reagendadas
DROP FUNCTION IF EXISTS seleccionar_entregas_reagendadas();

CREATE OR REPLACE FUNCTION seleccionar_entregas_reagendadas()
RETURNS TABLE (
    id_entrega INTEGER,
    cliente TEXT,
    tipo_entrega TEXT
)
LANGUAGE sql
AS $$
    SELECT 
        e.id_entrega, 
        c.nombre, 
        t.nombre
    FROM entregas e
    JOIN clientes c ON e.id_cliente = c.id_cliente
    JOIN cat_tipos_entrega t ON e.id_tipo_entrega = t.id_tipo_entrega
    WHERE e.id_estado_entrega = 3;
$$;




-- seleccionar entregas terminadas
CREATE OR REPLACE FUNCTION seleccionar_entregas_terminadas()
RETURNS TABLE (
    cliente TEXT,
    tipo_entrega TEXT
)
LANGUAGE sql
AS $$
    SELECT c.nombre, t.nombre
    FROM entregas e
    JOIN clientes c ON e.id_cliente = c.id_cliente
    JOIN cat_tipos_entrega t ON e.id_tipo_entrega = t.id_tipo_entrega
    WHERE e.id_estado_entrega = 2; -- estado : entregada
$$;

-- seleccionar repartidores libres
CREATE OR REPLACE FUNCTION seleccionar_repartidores_libres()
RETURNS TABLE (
    id_repartidor INT,  
    nombre TEXT,
    telefono TEXT
)
LANGUAGE sql
AS $$
    SELECT id_repartidor, nombre, telefono
    FROM repartidores
    WHERE activo = TRUE;
$$;

-- seleccionar vehiculo
CREATE OR REPLACE FUNCTION seleccionar_vehiculos_libres()
RETURNS TABLE (
    id_vehiculo INT,
    id_tipo_vehiculo INT,  
    modelo TEXT,
    id_repartidor_actual INT
)
LANGUAGE sql
AS $$
    SELECT id_vehiculo, id_tipo_vehiculo ,modelo, id_repartidor_actual
    FROM vehiculos
    WHERE id_estatus_vehiculo = 1;
$$;

-- seleccionar tipo de entrega
CREATE OR REPLACE FUNCTION seleccionar_tipo_de_entrega()
RETURNS TABLE (
    nombre TEXT
)
LANGUAGE sql
AS $$
    SELECT nombre FROM cat_tipos_entrega;
$$;

-- ================================================================================================
--                                       Valores por defecto
-- =================================================================================================

call insertar_tipo_licencia('moto');
call insertar_tipo_licencia('carro');

call insertar_tipo_vehiculo('moto');
call insertar_tipo_vehiculo('carro');

call insertar_estatus_vehiculo('libre');
call insertar_estatus_vehiculo('ocupado');

call insertar_tipo_entrega('campo');
call insertar_tipo_entrega('masivo');

call insertar_estado_entrega('pendiente');
call insertar_estado_entrega('entregada');
call insertar_estado_entrega('reagendar');

call insertar_repartidor('Luis Martínez', '555-123-4567');
call insertar_repartidor('Lalo Martínez', '555-123-4568');
call insertar_repartidor('Emma Martínez', '555-123-4569');
call insertar_repartidor('Paco Martínez', '555-123-4561');

call insertar_licencia_a_repartidor(1,1);
call insertar_licencia_a_repartidor(1,2);
call insertar_licencia_a_repartidor(2,1);
call insertar_licencia_a_repartidor(2,2);
call insertar_licencia_a_repartidor(3,1);
call insertar_licencia_a_repartidor(3,2);
call insertar_licencia_a_repartidor(4,1);
call insertar_licencia_a_repartidor(4,2);

call insertar_vehiculo(2, 'Nissan Versa', 18.5, 1);
call insertar_vehiculo(1, 'Italika 150', 35.0, 1);

call insertar_cliente('Cesar Zamudio','555-111-2222');
call insertar_cliente('Juan', '555-111-2222');
call insertar_cliente('Angel', '555-111-2222');
call insertar_cliente('Carlos', '555-111-2222');
call insertar_cliente('Pedro', '555-111-2222');
call insertar_cliente('Rafa', '555-111-2220');

call insertar_direccion(1,'Av. Juárez', '101', 'B', 'Centro', 'Cuauhtémoc', '06010', 'México');
call insertar_direccion(2,'Av. Juárez', '101', 'B', 'Centro', 'Cuauhtémoc', '06010', 'México');
call insertar_direccion(3,'Av. Juárez', '101', 'B', 'Centro', 'Cuauhtémoc', '06010', 'México');
call insertar_direccion(4,'Av. Juárez', '101', 'B', 'Centro', 'Cuauhtémoc', '06010', 'México');
call insertar_direccion(5,'Av. Juárez', '101', 'B', 'Centro', 'Cuauhtémoc', '06010', 'México');
call insertar_direccion(6,'Av. Juárez', '101', 'B', 'Centro', 'Cuauhtémoc', '06010', 'México');

call insertar_entrega(1,1,1,'un play 1',300);
call insertar_entrega(2,2,1,'un play 2',500);
call insertar_entrega(3,3,1,'un play 3',1200);
call insertar_entrega(4,4,2,'un play 4',3000);
call insertar_entrega(5,5,2,'un play 5',15000);
call insertar_entrega(6,6,2,'un play psp',3000);

--call actualizar_reagendado_a_pendiente();

call marcar_entrega_terminada(1);








