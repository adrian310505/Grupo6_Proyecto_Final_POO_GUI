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
# servicios/ServicioHotel.py
# Clase controladora principal. Hereda de QMainWindow.
# Conecta la interfaz gráfica con el DAO y el dominio.
# Implementa las 4 operaciones CRUD y validaciones de campos.
# ─────────────────────────────────────────────────────────────────

import re

from PySide6.QtWidgets import (QMainWindow, QMessageBox,
                                QTableWidgetItem, QHeaderView)
from PySide6.QtCore import Qt

from Gui.vtn_principal import Ui_ServicioHotel
from dominio.servicio_hotel import ServicioHotel as ServicioHotelDominio
from datos.ServicioHotel_DAO import ServicioHotel_DAO

# Expresión regular para validar correo electrónico
PATRON_CORREO = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'


class ServicioHotel(QMainWindow):
    """
    Ventana principal del sistema.
    Gestiona las operaciones CRUD: Guardar, Mostrar, Actualizar, Eliminar.
    """

    def __init__(self):
        super().__init__()
        self.ui = Ui_ServicioHotel()
        self.ui.setupUi(self)
        self.setWindowTitle("Sistema de Gestión de Servicios de Hotel")

        # Configurar encabezados de la tabla
        self.ui.tbl_servicios.setHorizontalHeaderLabels(
            ["Código", "Descripción", "Precio Base", "Correo"]
        )
        self.ui.tbl_servicios.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        # Conectar botones con métodos
        self.ui.btn_guardar.clicked.connect(self.guardar_servicio)
        self.ui.btn_mostrar.clicked.connect(self.mostrar_servicios)
        self.ui.btn_actualizar.clicked.connect(self.actualizar_servicio)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_servicio)
        self.ui.btn_limpiar.clicked.connect(self.limpiar_campos)

        # Al hacer clic en una fila de la tabla, cargar datos en los campos
        self.ui.tbl_servicios.cellClicked.connect(self.cargar_fila_seleccionada)

        # Mostrar registros al iniciar
        self.mostrar_servicios()

    # ── Validación de campos ──────────────────────────────────────

    def validar_campos(self, codigo, descripcion, precio_txt, correo):
        """
        Valida los 4 campos antes de cualquier operación de BD.
        Lanza ValueError con mensaje específico si hay error.
        """
        # Código
        if codigo.strip() == "":
            raise ValueError("El campo CÓDIGO no puede estar vacío.")

        # Descripción
        if descripcion.strip() == "":
            raise ValueError("El campo DESCRIPCIÓN no puede estar vacío.")
        if len(descripcion.strip()) < 5:
            raise ValueError("La DESCRIPCIÓN debe tener al menos 5 caracteres.")

        # Precio base
        if precio_txt.strip() == "":
            raise ValueError("El campo PRECIO BASE no puede estar vacío.")
        try:
            precio = float(precio_txt)
        except ValueError:
            raise ValueError("El PRECIO BASE debe ser un número válido (ej: 85.50).")
        if precio <= 0:
            raise ValueError("El PRECIO BASE debe ser mayor a cero.")
        if precio > 99999:
            raise ValueError("El PRECIO BASE no puede superar 99,999.")

        # Correo con expresión regular
        if correo.strip() == "":
            raise ValueError("El campo CORREO no puede estar vacío.")
        if not re.match(PATRON_CORREO, correo.strip()):
            raise ValueError(
                "El CORREO no tiene formato válido.\n\n"
                "Ejemplos válidos:\n"
                "  • usuario@gmail.com\n"
                "  • nombre@hotmail.com\n"
                "  • estudiante@instituto.edu.ec"
            )
        return precio

    # ── CREATE: Guardar ───────────────────────────────────────────

    def guardar_servicio(self):
        """Lee los campos, valida y guarda el registro en la base de datos."""
        codigo      = self.ui.txt_Codigo.text()
        descripcion = self.ui.txt_descripcion.text()
        precio_txt  = self.ui.txt_precio_base.text()
        correo      = self.ui.txt_correo.text()

        try:
            precio = self.validar_campos(codigo, descripcion, precio_txt, correo)

            # Verificar que el código no exista ya en la BD
            existente = ServicioHotel_DAO.obtener_por_codigo(codigo)
            if existente:
                raise ValueError(f"Ya existe un servicio con el código '{codigo.upper()}'.")

            # Crear objeto de dominio
            nuevo = ServicioHotelDominio(
                codigo=codigo.strip(),
                descripcion=descripcion.strip(),
                precio_base=precio,
                correo=correo.strip()
            )

            # Insertar en la base de datos
            resultado = ServicioHotel_DAO.insertar(nuevo)
            if resultado == 1:
                self.ui.statusbar.showMessage(
                    f"✔ Servicio '{nuevo.codigo}' guardado correctamente.", 4000
                )
                self.limpiar_campos()
                self.mostrar_servicios()   # refrescar tabla
            else:
                QMessageBox.critical(self, "Error", "No se pudo guardar el registro.")

        except ValueError as e:
            QMessageBox.critical(self, "✘ Error de validación", str(e))

    # ── READ: Mostrar ─────────────────────────────────────────────

    def mostrar_servicios(self):
        """Consulta todos los registros de la BD y los carga en la tabla."""
        servicios = ServicioHotel_DAO.obtener_todos()

        # Limpiar tabla antes de cargar
        self.ui.tbl_servicios.setRowCount(0)

        for sv in servicios:
            fila = self.ui.tbl_servicios.rowCount()
            self.ui.tbl_servicios.insertRow(fila)
            self.ui.tbl_servicios.setItem(fila, 0, QTableWidgetItem(sv.codigo))
            self.ui.tbl_servicios.setItem(fila, 1, QTableWidgetItem(sv.descripcion))
            self.ui.tbl_servicios.setItem(fila, 2, QTableWidgetItem(f"${sv.precio_base:.2f}"))
            self.ui.tbl_servicios.setItem(fila, 3, QTableWidgetItem(sv.correo))

        self.ui.statusbar.showMessage(
            f"Total de registros: {len(servicios)}", 3000
        )

    # ── UPDATE: Actualizar ────────────────────────────────────────

    def actualizar_servicio(self):
        """
        Actualiza el registro cuyo código está en el campo txt_Codigo.
        El código NO se puede modificar (es la clave de búsqueda).
        """
        codigo      = self.ui.txt_Codigo.text()
        descripcion = self.ui.txt_descripcion.text()
        precio_txt  = self.ui.txt_precio_base.text()
        correo      = self.ui.txt_correo.text()

        try:
            precio = self.validar_campos(codigo, descripcion, precio_txt, correo)

            # Verificar que el registro exista
            existente = ServicioHotel_DAO.obtener_por_codigo(codigo)
            if not existente:
                raise ValueError(f"No se encontró un servicio con código '{codigo.upper()}'.")

            # Confirmar antes de actualizar
            respuesta = QMessageBox.question(
                self, "Confirmar actualización",
                f"¿Desea actualizar el servicio '{codigo.upper()}'?",
                QMessageBox.Yes | QMessageBox.No
            )
            if respuesta == QMessageBox.No:
                return

            # Crear objeto con datos nuevos
            actualizado = ServicioHotelDominio(
                codigo=codigo.strip(),
                descripcion=descripcion.strip(),
                precio_base=precio,
                correo=correo.strip()
            )

            resultado = ServicioHotel_DAO.actualizar(actualizado)
            if resultado >= 1:
                self.ui.statusbar.showMessage(
                    f"✔ Servicio '{actualizado.codigo}' actualizado correctamente.", 4000
                )
                self.limpiar_campos()
                self.mostrar_servicios()
            else:
                QMessageBox.critical(self, "Error", "No se pudo actualizar el registro.")

        except ValueError as e:
            QMessageBox.critical(self, "✘ Error de validación", str(e))

    # ── DELETE: Eliminar ──────────────────────────────────────────

    def eliminar_servicio(self):
        """
        Elimina el registro cuyo código está en txt_Codigo.
        Solicita confirmación antes de proceder.
        """
        codigo = self.ui.txt_Codigo.text().strip()

        if not codigo:
            QMessageBox.warning(self, "Campo vacío",
                                "Ingrese el CÓDIGO del servicio a eliminar.")
            return

        # Verificar que exista
        existente = ServicioHotel_DAO.obtener_por_codigo(codigo)
        if not existente:
            QMessageBox.warning(self, "No encontrado",
                                f"No existe un servicio con código '{codigo.upper()}'.")
            return

        # Solicitar confirmación
        respuesta = QMessageBox.question(
            self, "Confirmar eliminación",
            f"¿Está seguro de eliminar el servicio '{codigo.upper()}'?\n"
            f"Esta acción no se puede deshacer.",
            QMessageBox.Yes | QMessageBox.No
        )
        if respuesta == QMessageBox.No:
            return

        resultado = ServicioHotel_DAO.eliminar(codigo)
        if resultado >= 1:
            self.ui.statusbar.showMessage(
                f"✔ Servicio '{codigo.upper()}' eliminado correctamente.", 4000
            )
            self.limpiar_campos()
            self.mostrar_servicios()
        else:
            QMessageBox.critical(self, "Error", "No se pudo eliminar el registro.")

    # ── Cargar fila al hacer clic en la tabla ─────────────────────

    def cargar_fila_seleccionada(self, fila):
        """
        Al hacer clic en una fila de la tabla, carga los datos
        en los campos de texto para facilitar actualización o eliminación.
        """
        codigo      = self.ui.tbl_servicios.item(fila, 0).text()
        descripcion = self.ui.tbl_servicios.item(fila, 1).text()
        precio      = self.ui.tbl_servicios.item(fila, 2).text().replace("$", "")
        correo      = self.ui.tbl_servicios.item(fila, 3).text()

        self.ui.txt_Codigo.setText(codigo)
        self.ui.txt_descripcion.setText(descripcion)
        self.ui.txt_precio_base.setText(precio)
        self.ui.txt_correo.setText(correo)

    # ── Limpiar campos ────────────────────────────────────────────

    def limpiar_campos(self):
        """Limpia todos los campos de texto del formulario."""
        self.ui.txt_Codigo.clear()
        self.ui.txt_descripcion.clear()
        self.ui.txt_precio_base.clear()
        self.ui.txt_correo.clear()
        self.ui.tbl_servicios.clearSelection()
        self.ui.txt_Codigo.setFocus()
