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
# datos/conexion.py
# Conexión a SQL Server local usando Autenticación de Windows.
# Servidor : DESKTOP-8VUL47D
# Base de datos: master
# No requiere usuario ni contraseña (Trusted_Connection).
# ─────────────────────────────────────────────────────────────────

import sys
import pyodbc as bd


class Conexion:
    """Clase Singleton que gestiona la conexión a SQL Server con Windows Auth."""

    _SERVIDOR = 'DESKTOP-8VUL47D'   # Nombre del servidor SQL Server local
    _BBDD     = 'master'             # Base de datos donde está la tabla
    _conexion = None
    _cursor   = None

    @classmethod
    def obtener_conexion(cls):
        """Retorna la conexión activa; la crea si no existe."""
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(
                    'DRIVER={ODBC Driver 17 for SQL Server};'
                    f'SERVER={cls._SERVIDOR};'
                    f'DATABASE={cls._BBDD};'
                    'Trusted_Connection=yes;'
                    'TrustServerCertificate=yes;'
                )
                print(f"Conexión exitosa → {cls._SERVIDOR} / {cls._BBDD}")
                return cls._conexion
            except Exception as e:
                print(f"Error de conexión: {e}")
                sys.exit()
        return cls._conexion

    @classmethod
    def obtener_cursor(cls):
        """Retorna el cursor activo; lo crea si no existe."""
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtener_conexion().cursor()
                return cls._cursor
            except Exception as e:
                print(f"Error al obtener cursor: {e}")
                sys.exit()
        return cls._cursor

    @classmethod
    def cerrar_conexion(cls):
        """Cierra el cursor y la conexión."""
        if cls._cursor:
            cls._cursor.close()
            cls._cursor = None
        if cls._conexion:
            cls._conexion.close()
            cls._conexion = None


if __name__ == '__main__':
    # Prueba rápida de conexión
    con = Conexion.obtener_conexion()
    cur = Conexion.obtener_cursor()
    cur.execute("SELECT name FROM sys.tables WHERE name = 'servicios_hotel'")
    tabla = cur.fetchone()
    if tabla:
        print("Tabla 'servicios_hotel' encontrada correctamente.")
    else:
        print("ADVERTENCIA: la tabla 'servicios_hotel' no existe en master.")
