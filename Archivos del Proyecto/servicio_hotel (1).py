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
# dominio/servicio_hotel.py
# Superclase del dominio con encapsulamiento completo.
# Representa un servicio del hotel con sus 4 atributos principales.
# ─────────────────────────────────────────────────────────────────


class ServicioHotel:
    """Clase de dominio que representa un servicio del hotel."""

    def __init__(self, codigo, descripcion, precio_base, correo):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio_base = precio_base
        self.correo = correo

    # ── codigo ────────────────────────────────────────────────────
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if not valor or str(valor).strip() == "":
            raise ValueError("El código no puede estar vacío.")
        self._codigo = str(valor).strip().upper()

    # ── descripcion ───────────────────────────────────────────────
    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor):
        if not valor or str(valor).strip() == "":
            raise ValueError("La descripción no puede estar vacía.")
        self._descripcion = str(valor).strip()

    # ── precio_base ───────────────────────────────────────────────
    @property
    def precio_base(self):
        return self._precio_base

    @precio_base.setter
    def precio_base(self, valor):
        try:
            v = float(valor)
        except (ValueError, TypeError):
            raise ValueError("El precio base debe ser un número válido.")
        if v < 0:
            raise ValueError("El precio base no puede ser negativo.")
        self._precio_base = v

    # ── correo ────────────────────────────────────────────────────
    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if not valor or str(valor).strip() == "":
            raise ValueError("El correo no puede estar vacío.")
        self._correo = str(valor).strip().lower()

    def __str__(self):
        return (f"[{self._codigo}] {self._descripcion} "
                f"| Precio: ${self._precio_base:.2f} | Correo: {self._correo}")
