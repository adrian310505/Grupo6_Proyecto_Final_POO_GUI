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
# main.py
# Punto de entrada de la aplicación.
# Inicializa QApplication y muestra la ventana principal.
# ─────────────────────────────────────────────────────────────────

import sys

from PySide6.QtWidgets import QApplication

from servicio.ServicioHotel import ServicioHotel

app = QApplication(sys.argv)
vtn_principal = ServicioHotel()
vtn_principal.show()
sys.exit(app.exec())
