-- =============================================
-- BASE DE DATOS DELIVERY COMPLETA
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
--INSERT INTO cat_estados_entrega (nombre) VALUES ('pendiente'), ('entregada'), ('esatica');

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

-- =============================================
-- Procesamiento almacenado
-- =============================================
-- Para agregar elementos al catalogo tipo de licencia
CREATE OR REPLACE PROCEDURE agregar_tipo_licencia(
    IN p_nombre TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM cat_tipos_licencia WHERE nombre = p_nombre
    ) THEN
        RAISE EXCEPTION 'Ya existe un tipo de licencia con ese nombre.';
    END IF;

    INSERT INTO cat_tipos_licencia(nombre) VALUES (p_nombre);
    RAISE NOTICE 'Tipo de licencia "%" agregado.', p_nombre;
END;
$$;

-- Para agregar elementos al catalogo tipo de vehiculo
CREATE OR REPLACE PROCEDURE agregar_tipo_vehiculo(
    IN p_nombre TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM cat_tipos_vehiculo WHERE nombre = p_nombre
    ) THEN
        RAISE EXCEPTION 'Ya existe un tipo de vehículo con ese nombre.';
    END IF;

    INSERT INTO cat_tipos_vehiculo(nombre) VALUES (p_nombre);
    RAISE NOTICE 'Tipo de vehículo "%" agregado.', p_nombre;
END;
$$;

-- Para agregar elementos al catalogo estatus del vehiculo
CREATE OR REPLACE PROCEDURE agregar_estatus_vehiculo(
    IN p_nombre TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM cat_estatus_vehiculo WHERE nombre = p_nombre
    ) THEN
        RAISE EXCEPTION 'Ya existe un estatus de vehículo con ese nombre.';
    END IF;

    INSERT INTO cat_estatus_vehiculo(nombre) VALUES (p_nombre);
    RAISE NOTICE 'Estatus de vehículo "%" agregado.', p_nombre;
END;
$$;

-- Para agregar elementos al catalogo tipo de entrega
CREATE OR REPLACE PROCEDURE agregar_tipo_entrega(
    IN p_nombre TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM cat_tipos_entrega WHERE nombre = p_nombre
    ) THEN
        RAISE EXCEPTION 'Ya existe un tipo de entrega con ese nombre.';
    END IF;

    INSERT INTO cat_tipos_entrega(nombre) VALUES (p_nombre);
    RAISE NOTICE 'Tipo de entrega "%" agregado.', p_nombre;
END;
$$;

-- Para agregar elementos al catalogo de estado
CREATE OR REPLACE PROCEDURE agregar_estado_entrega(
    IN p_nombre TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM cat_estados_entrega WHERE nombre = p_nombre
    ) THEN
        RAISE EXCEPTION 'Ya existe un estado de entrega con ese nombre.';
    END IF;

    INSERT INTO cat_estados_entrega(nombre) VALUES (p_nombre);
    RAISE NOTICE 'Estado de entrega "%" agregado.', p_nombre;
END;
$$;

-- Nos regresara un arreglo y tendremos las entregas pendientes para la primera pantalla
CREATE OR REPLACE FUNCTION obtener_entregas_pendientes()
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
    WHERE e.id_estado_entrega = 1; -- estado pendiente
$$;

-- Nos regresara un arreglo y tendremos las entregas pendientes para la primera pantalla
CREATE OR REPLACE FUNCTION obtener_entregas_entregadas()
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

-- Con esto creamos una entrega sin su repartidor aún, para asi guardalo
CREATE OR REPLACE PROCEDURE crear_entrega_completa(
    IN p_nombre_cliente TEXT,
    IN p_telefono_cliente TEXT,
    IN p_calle TEXT,
    IN p_num_ext TEXT,
    IN p_num_int TEXT,
    IN p_colonia TEXT,
    IN p_municipio TEXT,
    IN p_cp TEXT,
    IN p_pais TEXT,
    IN p_id_tipo_entrega INT,
    IN p_beneficio TEXT,
    IN p_monto NUMERIC
)
LANGUAGE plpgsql
AS $$
DECLARE
    cliente_id INT;
    direccion_id INT;
BEGIN
    -- Validar CP
    IF p_cp !~ '^[0-9]{5}$' THEN
        RAISE EXCEPTION 'Código postal inválido: %', p_cp;
    END IF;

    -- Buscar cliente
    SELECT id_cliente INTO cliente_id
    FROM clientes
    WHERE nombre = p_nombre_cliente AND telefono = p_telefono_cliente;

    -- Si no existe, lo crea
    IF cliente_id IS NULL THEN
        INSERT INTO clientes (nombre, telefono)
        VALUES (p_nombre_cliente, p_telefono_cliente)
        RETURNING id_cliente INTO cliente_id;
    END IF;

    -- Crear dirección
    INSERT INTO direcciones (
        id_cliente, calle, num_ext, num_int, colonia, delegacion_municipio, cp, pais
    ) VALUES (
        cliente_id, p_calle, p_num_ext, p_num_int, p_colonia, p_municipio, p_cp, p_pais
    ) RETURNING id_direccion INTO direccion_id;

    -- Crear entrega
    INSERT INTO entregas (
        id_cliente, id_direccion, id_tipo_entrega, id_estado_entrega,
        beneficios, monto_beneficio
    ) VALUES (
        cliente_id, direccion_id, p_id_tipo_entrega, 3,
        p_beneficio, p_monto
    );
END;
$$;

-- Para editar TODOS los campos que se ingreso:
CREATE OR REPLACE PROCEDURE editar_entrega_completa(
    IN p_id_entrega INT,
    IN p_nombre_cliente TEXT,
    IN p_telefono_cliente TEXT,
    IN p_calle TEXT,
    IN p_num_ext TEXT,
    IN p_num_int TEXT,
    IN p_colonia TEXT,
    IN p_municipio TEXT,
    IN p_cp TEXT,
    IN p_pais TEXT,
    IN p_id_tipo_entrega INT,
    IN p_beneficio TEXT,
    IN p_monto NUMERIC
)
LANGUAGE plpgsql
AS $$
DECLARE
    cliente_id INT;
    direccion_id INT;
BEGIN
    -- Validar que la entrega esté estatica
    SELECT id_cliente, id_direccion INTO cliente_id, direccion_id
    FROM entregas
    WHERE id_entrega = p_id_entrega AND id_estado_entrega = 3;

    IF cliente_id IS NULL THEN
        RAISE EXCEPTION 'Solo se pueden editar entregas estaticas.';
    END IF;

    -- Validar CP
    IF p_cp !~ '^[0-9]{5}$' THEN
        RAISE EXCEPTION 'Código postal inválido: %', p_cp;
    END IF;

    -- Actualizar cliente (nombre y teléfono)
    UPDATE clientes
    SET nombre = p_nombre_cliente,
        telefono = p_telefono_cliente
    WHERE id_cliente = cliente_id;

    -- Actualizar dirección
    UPDATE direcciones
    SET calle = p_calle,
        num_ext = p_num_ext,
        num_int = p_num_int,
        colonia = p_colonia,
        delegacion_municipio = p_municipio,
        cp = p_cp,
        pais = p_pais
    WHERE id_direccion = direccion_id;

    -- Actualizar entrega
    UPDATE entregas
    SET id_tipo_entrega = p_id_tipo_entrega,
        beneficios = p_beneficio,
        monto_beneficio = p_monto
    WHERE id_entrega = p_id_entrega;
END;
$$;

--Para eliminar una entrega
CREATE OR REPLACE PROCEDURE eliminar_entrega_completa(
    IN p_id_entrega INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    cliente_id INT;
    direccion_id INT;
    entregas_restantes INT;
BEGIN
    -- Validar que la entrega esté pendiente
    SELECT id_cliente, id_direccion INTO cliente_id, direccion_id
    FROM entregas
    WHERE id_entrega = p_id_entrega AND id_estado_entrega = 3;

    IF cliente_id IS NULL THEN
        RAISE EXCEPTION 'Solo se pueden eliminar entregas estaticas.';
    END IF;

    -- Eliminar entrega
    DELETE FROM entregas WHERE id_entrega = p_id_entrega;

    -- Eliminar dirección
    DELETE FROM direcciones WHERE id_direccion = direccion_id;

    -- Verificar si el cliente tiene otras entregas
    SELECT COUNT(*) INTO entregas_restantes
    FROM entregas
    WHERE id_cliente = cliente_id;

    -- Si no tiene más entregas, eliminar cliente
    IF entregas_restantes = 0 THEN
        DELETE FROM clientes WHERE id_cliente = cliente_id;
    END IF;
END;
$$;

--- Para los repartidores libres
CREATE OR REPLACE FUNCTION obtener_repartidores_libres()
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

-- Para pasar las entregas a pendientes y pasen a la primera pantalla
CREATE OR REPLACE PROCEDURE estaticas_a_pendientes()
LANGUAGE plpgsql
AS $$
DECLARE
    estado_estatica INT := 3;
    estado_pendiente INT := 1;
BEGIN
    -- Validar que existan entregas en estado estático
    IF NOT EXISTS (
        SELECT 1 FROM entregas WHERE id_estado_entrega = estado_estatica
    ) THEN
        RAISE NOTICE 'No hay entregas en estado estático para reactivar.';
        RETURN;
    END IF;

    -- Actualizar todas las entregas estáticas a pendientes
    UPDATE entregas
    SET id_estado_entrega = estado_pendiente
    WHERE id_estado_entrega = estado_estatica;

    RAISE NOTICE 'Todas las entregas estáticas cambiaron a pendientes.';
END;
$$;

--Para asignar un repartidor a n entregas
CREATE OR REPLACE PROCEDURE asignar_entregas_a_repartidor(
    IN p_id_repartidor INT,
    IN p_entregas INT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_id_vehiculo INT;
    v_id_entrega INT;
    v_asignadas INT := 0;
BEGIN
    -- Validar que el repartidor esté activo
    IF NOT EXISTS (
        SELECT 1 FROM repartidores WHERE id_repartidor = p_id_repartidor AND activo = TRUE
    ) THEN
        RAISE EXCEPTION 'El repartidor % no está disponible.', p_id_repartidor;
    END IF;

    -- Obtener vehículo asignado al repartidor
    SELECT id_vehiculo INTO v_id_vehiculo
    FROM vehiculos
    WHERE id_repartidor_actual = p_id_repartidor;

    IF v_id_vehiculo IS NULL THEN
        RAISE EXCEPTION 'El repartidor % no tiene vehículo asignado.', p_id_repartidor;
    END IF;

    -- Asignar entregas en lote
    FOREACH v_id_entrega IN ARRAY p_entregas LOOP
        -- Validar que la entrega esté pendiente
        IF EXISTS (
            SELECT 1 FROM entregas
            WHERE id_entrega = v_id_entrega AND id_estado_entrega = 1
        ) THEN
            UPDATE entregas
            SET id_repartidor_asignado = p_id_repartidor,
                id_vehiculo_asignado = v_id_vehiculo
            WHERE id_entrega = v_id_entrega;

            v_asignadas := v_asignadas + 1;
        ELSE
            RAISE NOTICE 'Entrega % no está pendiente. Se omitió.', v_id_entrega;
        END IF;
    END LOOP;

    -- Marcar repartidor como ocupado solo si se asignó al menos una entrega
    IF v_asignadas > 0 THEN
        UPDATE repartidores
        SET activo = FALSE
        WHERE id_repartidor = p_id_repartidor;

        RAISE NOTICE 'Se asignaron % entregas al repartidor % con vehículo %.', v_asignadas, p_id_repartidor, v_id_vehiculo;
    ELSE
        RAISE NOTICE 'No se asignó ninguna entrega. El repartidor sigue disponible.';
    END IF;
END;
$$;

-- Para crear un repartidor
CREATE OR REPLACE PROCEDURE crear_repartidor(
    IN p_nombre TEXT,
    IN p_telefono TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Validar que no exista el teléfono
    IF EXISTS (
        SELECT 1 FROM repartidores WHERE telefono = p_telefono
    ) THEN
        RAISE EXCEPTION 'Ya existe un repartidor con ese teléfono.';
    END IF;

    -- Insertar repartidor
    INSERT INTO repartidores (nombre, telefono, activo)
    VALUES (p_nombre, p_telefono, TRUE);

    RAISE NOTICE 'Repartidor % creado correctamente.', p_nombre;
END;
$$;

--- Para guardar las licencias de cada repartidor
CREATE OR REPLACE PROCEDURE guardar_licencia_repartidor(
    IN p_id_repartidor INT,
    IN p_id_tipo_licencia INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Validar existencia de repartidor
    IF NOT EXISTS (
        SELECT 1 FROM repartidores WHERE id_repartidor = p_id_repartidor
    ) THEN
        RAISE EXCEPTION 'El repartidor % no existe.', p_id_repartidor;
    END IF;

    -- Validar existencia de tipo de licencia
    IF NOT EXISTS (
        SELECT 1 FROM cat_tipos_licencia WHERE id_tipo_licencia = p_id_tipo_licencia
    ) THEN
        RAISE EXCEPTION 'El tipo de licencia % no existe.', p_id_tipo_licencia;
    END IF;

    -- Validar que no esté duplicado
    IF EXISTS (
        SELECT 1 FROM licencias_repartidor
        WHERE id_repartidor = p_id_repartidor AND id_tipo_licencia = p_id_tipo_licencia
    ) THEN
        RAISE EXCEPTION 'El repartidor ya tiene registrada esa licencia.';
    END IF;

    -- Insertar licencia
    INSERT INTO licencias_repartidor (id_repartidor, id_tipo_licencia)
    VALUES (p_id_repartidor, p_id_tipo_licencia);

    RAISE NOTICE 'Licencia % registrada para repartidor %.', p_id_tipo_licencia, p_id_repartidor;
END;
$$;

-- Para guardar vehiculos nuevos a nuestra empresa osi osi osi
CREATE OR REPLACE PROCEDURE guardar_vehiculo(
    IN p_id_tipo_vehiculo INT,
    IN p_modelo TEXT,
    IN p_km_por_litro NUMERIC,
    IN p_id_estatus_vehiculo INT,
    IN p_id_repartidor_actual INT DEFAULT NULL
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Validar tipo de vehículo
    IF NOT EXISTS (
        SELECT 1 FROM cat_tipos_vehiculo WHERE id_tipo_vehiculo = p_id_tipo_vehiculo
    ) THEN
        RAISE EXCEPTION 'Tipo de vehículo % no existe.', p_id_tipo_vehiculo;
    END IF;

    -- Validar estatus de vehículo
    IF NOT EXISTS (
        SELECT 1 FROM cat_estatus_vehiculo WHERE id_estatus_vehiculo = p_id_estatus_vehiculo
    ) THEN
        RAISE EXCEPTION 'Estatus de vehículo % no existe.', p_id_estatus_vehiculo;
    END IF;

    -- Validar repartidor si se proporciona
    IF p_id_repartidor_actual IS NOT NULL THEN
        IF NOT EXISTS (
            SELECT 1 FROM repartidores WHERE id_repartidor = p_id_repartidor_actual
        ) THEN
            RAISE EXCEPTION 'Repartidor % no existe.', p_id_repartidor_actual;
        END IF;
    END IF;

    -- Insertar vehículo
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

    RAISE NOTICE 'Vehículo "%" registrado correctamente.', p_modelo;
END;
$$;

--- Para asignar repartidores a vehiculos
CREATE OR REPLACE PROCEDURE asignar_vehiculo_a_repartidor(
    IN p_id_repartidor INT,
    IN p_id_vehiculo INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_tipo_vehiculo INT;
    v_tiene_moto BOOLEAN := FALSE;
    v_tiene_carro BOOLEAN := FALSE;
BEGIN
    -- Validar que el repartidor esté activo
    IF NOT EXISTS (
        SELECT 1 FROM repartidores WHERE id_repartidor = p_id_repartidor AND activo = TRUE
    ) THEN
        RAISE EXCEPTION 'El repartidor no está disponible.';
    END IF;

    -- Validar que el repartidor no tenga ya un vehículo asignado
    IF EXISTS (
        SELECT 1 FROM vehiculos WHERE id_repartidor_actual = p_id_repartidor
    ) THEN
        RAISE EXCEPTION 'El repartidor ya tiene un vehículo asignado.';
    END IF;

    -- Validar que el vehículo esté libre
    IF EXISTS (
        SELECT 1 FROM vehiculos WHERE id_vehiculo = p_id_vehiculo AND id_repartidor_actual IS NOT NULL
    ) THEN
        RAISE EXCEPTION 'El vehículo ya está asignado.';
    END IF;

    -- Obtener tipo de vehículo
    SELECT id_tipo_vehiculo INTO v_tipo_vehiculo
    FROM vehiculos
    WHERE id_vehiculo = p_id_vehiculo;

    -- Verificar licencias del repartidor
    SELECT EXISTS (
        SELECT 1 FROM licencias_repartidor
        WHERE id_repartidor = p_id_repartidor AND id_tipo_licencia = 1 -- moto
    ) INTO v_tiene_moto;

    SELECT EXISTS (
        SELECT 1 FROM licencias_repartidor
        WHERE id_repartidor = p_id_repartidor AND id_tipo_licencia = 2 -- carro
    ) INTO v_tiene_carro;

    -- Validar compatibilidad
    IF v_tipo_vehiculo = 1 AND NOT v_tiene_moto THEN
        RAISE EXCEPTION 'El repartidor no tiene licencia para moto.';
    ELSIF v_tipo_vehiculo = 2 AND NOT v_tiene_carro THEN
        RAISE EXCEPTION 'El repartidor no tiene licencia para carro.';
    END IF;

    -- Asignar vehículo
    UPDATE vehiculos
    SET id_repartidor_actual = p_id_repartidor,
        id_estatus_vehiculo = 2 -- ocupado
    WHERE id_vehiculo = p_id_vehiculo;

    RAISE NOTICE 'Vehículo % asignado al repartidor %.', p_id_vehiculo, p_id_repartidor;
END;
$$;

-- ==========================================================================================
-- = Para hacer registros de prueba
-- ====================================================================================
-- Para los valores por defecto
CALL agregar_tipo_licencia('moto');
CALL agregar_tipo_licencia('carro');

CALL agregar_tipo_vehiculo('moto');
CALL agregar_tipo_vehiculo('carro');

CALL agregar_estatus_vehiculo('libre');
CALL agregar_estatus_vehiculo('ocupado');

CALL agregar_tipo_entrega('campo');
CALL agregar_tipo_entrega('masivo');

CALL agregar_estado_entrega('pendiente');
CALL agregar_estado_entrega('entregado');
CALL agregar_estado_entrega('estatica');

-- Para ingresar repartidores
CALL crear_repartidor('Luis Martínez', '555-123-4567');
CALL crear_repartidor('Lalo Martínez', '555-123-4568');
CALL crear_repartidor('Emma Martínez', '555-123-4569');
CALL crear_repartidor('Paco Martínez', '555-123-4561');

-- Para agregarles licencia
CALL guardar_licencia_repartidor(1, 1);
CALL guardar_licencia_repartidor(1, 2);
CALL guardar_licencia_repartidor(2, 1);
CALL guardar_licencia_repartidor(3, 2);
CALL guardar_licencia_repartidor(3, 1);
CALL guardar_licencia_repartidor(3, 2);
CALL guardar_licencia_repartidor(4, 1);
CALL guardar_licencia_repartidor(4, 2);

-- Creamos carros que tenemos
CALL guardar_vehiculo(2, 'Nissan Versa', 18.5, 1); -- tipo carro, libre
CALL guardar_vehiculo(1, 'Italika 150', 35.0, 2); -- tipo moto, ocupada, asignada a repartidor 4

-- Para los clientes
CALL crear_entrega_completa('Cesar Zamudio', '555-111-2222','Av. Juárez', '101', 'B', 'Centro', 
	'Cuauhtémoc', '06010', 'México',1, 'Entrega de apoyo alimentario', 450.00);
CALL crear_entrega_completa('Juan', '555-111-2222','Av. Juárez', '101', 'B', 'Centro', 
	'Cuauhtémoc', '06010', 'México',2, 'Plan EAT', 50.00);
CALL crear_entrega_completa('Angel', '555-111-2222','Av. Juárez', '101', 'B', 'Centro', 
	'Cuauhtémoc', '06010', 'México',2, 'Un sillon', 4500.00);
CALL crear_entrega_completa('Carlos', '555-111-2222','Av. Juárez', '101', 'B', 'Centro', 
	'Cuauhtémoc', '06010', 'México',1, 'Una laptop', 4350.00);
CALL crear_entrega_completa('Pedro', '555-111-2222','Av. Juárez', '101', 'B', 'Centro', 
	'Cuauhtémoc', '06010', 'México',1, 'Entrega de apoyo alimentario', 450.00);


