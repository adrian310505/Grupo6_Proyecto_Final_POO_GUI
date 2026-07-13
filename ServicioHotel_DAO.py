# Proyecto Segundo Parcial - GUI con Base de Datos
# Asignatura: Programación Orientada a Objetos
# Jornada: Matutina
# Grupo: 6
# Integrantes:
# - Luna Henry
# - Sánchez Adrian
# - Merchán Evelyn
# - Veintimilla Alejandra
# - Rodríguez Nayeli

# ─────────────────────────────────────────────────────────────────
# datos/ServicioHotel_DAO.py
# Clase DAO (Data Access Object) que implementa las 4 operaciones
# CRUD sobre la tabla 'servicios_hotel' en SQL Server.
# ─────────────────────────────────────────────────────────────────

from datos.conexion import Conexion
from dominio.servicio_hotel import ServicioHotel


class ServicioHotel_DAO:
    """Gestiona las operaciones CRUD de ServicioHotel en la base de datos."""

    # ── Sentencias SQL ────────────────────────────────────────────
    _INSERT = ("INSERT INTO servicios_hotel (codigo, descripcion, precio_base, correo) "
               "VALUES (?, ?, ?, ?)")

    _SELECT_ALL = ("SELECT codigo, descripcion, precio_base, correo "
                   "FROM servicios_hotel ORDER BY codigo")

    _SELECT_BY_CODIGO = ("SELECT codigo, descripcion, precio_base, correo "
                         "FROM servicios_hotel WHERE codigo = ?")

    _UPDATE = ("UPDATE servicios_hotel "
               "SET descripcion = ?, precio_base = ?, correo = ? "
               "WHERE codigo = ?")

    _DELETE = "DELETE FROM servicios_hotel WHERE codigo = ?"

    # ── CREATE: Insertar un nuevo registro ────────────────────────
    @classmethod
    def insertar(cls, servicio: ServicioHotel) -> int:
        """
        Inserta un nuevo servicio en la base de datos.
        Retorna 1 si fue exitoso, -1 si hubo error.
        """
        try:
            cursor = Conexion.obtener_cursor()
            datos = (
                servicio.codigo,
                servicio.descripcion,
                servicio.precio_base,
                servicio.correo
            )
            cursor.execute(cls._INSERT, datos)
            Conexion.obtener_conexion().commit()   # confirmar transacción
            return cursor.rowcount
        except Exception as e:
            print(f"Error al insertar: {e}")
            return -1

    # ── READ: Obtener todos los registros ─────────────────────────
    @classmethod
    def obtener_todos(cls) -> list:
        """
        Obtiene todos los servicios almacenados en la base de datos.
        Retorna una lista de objetos ServicioHotel.
        """
        servicios = []
        try:
            cursor = Conexion.obtener_cursor()
            cursor.execute(cls._SELECT_ALL)
            filas = cursor.fetchall()
            for fila in filas:
                # Crear objeto de dominio por cada fila
                sv = ServicioHotel(
                    codigo=fila[0],
                    descripcion=fila[1],
                    precio_base=fila[2],
                    correo=fila[3]
                )
                servicios.append(sv)
        except Exception as e:
            print(f"Error al obtener registros: {e}")
        return servicios

    # ── READ: Obtener un registro por código ──────────────────────
    @classmethod
    def obtener_por_codigo(cls, codigo: str):
        """
        Busca un servicio por su código.
        Retorna el objeto ServicioHotel o None si no existe.
        """
        try:
            cursor = Conexion.obtener_cursor()
            cursor.execute(cls._SELECT_BY_CODIGO, (codigo.upper(),))
            fila = cursor.fetchone()
            if fila:
                return ServicioHotel(
                    codigo=fila[0],
                    descripcion=fila[1],
                    precio_base=fila[2],
                    correo=fila[3]
                )
        except Exception as e:
            print(f"Error al buscar por código: {e}")
        return None

    # ── UPDATE: Actualizar un registro existente ──────────────────
    @classmethod
    def actualizar(cls, servicio: ServicioHotel) -> int:
        """
        Actualiza descripcion, precio_base y correo de un servicio
        identificado por su codigo.
        Retorna 1 si fue exitoso, -1 si hubo error.
        """
        try:
            cursor = Conexion.obtener_cursor()
            datos = (
                servicio.descripcion,
                servicio.precio_base,
                servicio.correo,
                servicio.codigo     # WHERE codigo = ?
            )
            cursor.execute(cls._UPDATE, datos)
            Conexion.obtener_conexion().commit()
            return cursor.rowcount
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return -1

    # ── DELETE: Eliminar un registro ──────────────────────────────
    @classmethod
    def eliminar(cls, codigo: str) -> int:
        """
        Elimina el servicio con el código indicado.
        Retorna 1 si fue exitoso, -1 si hubo error.
        """
        try:
            cursor = Conexion.obtener_cursor()
            cursor.execute(cls._DELETE, (codigo.upper(),))
            Conexion.obtener_conexion().commit()
            return cursor.rowcount
        except Exception as e:
            print(f"Error al eliminar: {e}")
            return -1
