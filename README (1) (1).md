# 🏨 Sistema de Gestión de Servicios de Hotel
### Proyecto Segundo Parcial — GUI con Base de Datos | POO | Grupo 6

---

## 📋 Descripción general

Aplicación de escritorio desarrollada en **Python con PySide6**, conectada a **SQL Server**, que permite gestionar servicios de un hotel mediante una interfaz gráfica con operaciones CRUD completas: registrar, consultar, actualizar y eliminar registros desde la GUI hacia la base de datos.

---

## 👥 Integrantes del grupo

| Nombre | Rol |
|---|---|
| Luna Henry | Integrante |
| Sánchez Adrian | Integrante |
| Merchán Evelyn | Integrante |
| Veintimilla Alejandra | Integrante |
| Rodríguez Nayeli | Integrante |

**Jornada:** Matutina | **Grupo:** 6

---

## ✅ Funcionalidades implementadas

| Operación | Descripción |
|---|---|
| **Guardar (CREATE)** | Registra un nuevo servicio en la base de datos con validaciones previas |
| **Mostrar (READ)** | Consulta y muestra todos los registros almacenados en la tabla |
| **Actualizar (UPDATE)** | Modifica descripción, precio y correo de un servicio existente |
| **Eliminar (DELETE)** | Borra un registro con confirmación previa del usuario |
| **Validaciones** | Campos obligatorios, precio positivo, correo con regex, código máx. 5 caracteres |

---

## 🛠️ Tecnologías utilizadas

- **Python 3.12+**
- **PySide6** — Interfaz gráfica de usuario
- **pyodbc** — Conexión a SQL Server
- **SQL Server** — Base de datos (ODBC Driver 17)
- **PyCharm** — Entorno de desarrollo

---

## ▶️ Instrucciones para ejecutar

1. Clonar el repositorio:
   ```bash
   git clone <url-repositorio>
   cd Proyecto_Gestion_de_hotel
   ```

2. Instalar dependencias:
   ```bash
   pip install PySide6 pyodbc
   ```

3. Crear la tabla en SQL Server ejecutando el script:
   ```
   crear_tabla.sql
   ```

4. Ejecutar la aplicación:
   ```bash
   python main.py
   ```

---

## 🗂️ Estructura del proyecto

```
Proyecto_Gestion_de_hotel/
│── main.py                        ← Punto de entrada
│── crear_tabla.sql                ← Script de creación de tabla
│── README.md
│── dominio/
│   ├── __init__.py
│   └── servicio_hotel.py          ← Clase de dominio con encapsulamiento
│── datos/
│   ├── __init__.py
│   ├── conexion.py                ← Conexión Singleton a SQL Server
│   └── ServicioHotel_DAO.py       ← Operaciones CRUD con la BD
│── servicios/
│   ├── __init__.py
│   └── ServicioHotel.py           ← Controlador GUI + lógica CRUD
└── Gui/
    ├── __init__.py
    ├── vtn_principal.ui           ← Diseño de la ventana (Qt Designer)
    └── vtn_principal.py           ← Generado desde el .ui
```

---

## 🗄️ Descripción de la base de datos

**Servidor:** 10.4.107.75  
**Base de datos:** SAP  
**Tabla:** `servicios_hotel`

| Campo | Tipo | Descripción |
|---|---|---|
| `codigo` | VARCHAR(5) PK | Código único del servicio (máx. 5 caracteres) |
| `descripcion` | VARCHAR(200) | Descripción del servicio |
| `precio_base` | DECIMAL(10,2) | Precio base del servicio |
| `correo` | VARCHAR(100) | Correo de contacto del servicio |

---

## 🔐 Validaciones implementadas

| Campo | Validación |
|---|---|
| **Código** | No vacío, máximo 5 caracteres (bloqueado en la UI) |
| **Descripción** | No vacía, mínimo 5 caracteres |
| **Precio base** | No vacío, debe ser número, mayor a cero, menor a 99,999 |
| **Correo** | Formato válido validado con expresión regular `r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'` |
| **Duplicados** | No permite guardar un código ya existente |
| **Eliminación** | Solicita confirmación antes de borrar |
| **Actualización** | Verifica que el código exista antes de modificar |

---

## 📸 Capturas de pantalla

- [Captura 1](https://drive.google.com/file/d/1JUkk70WLgDBUgtCewUQuPSnc0bCacnua/view?usp=drivesdk)
- [Captura 2](https://drive.google.com/file/d/1hfn0VRubrcw09msO3eMK6w8UHBbQMSvW/view?usp=drivesdk)
- [Captura 3](https://drive.google.com/file/d/13stNeN1-mIW9nUllYj2ubiiitjUmAPPS/view?usp=drivesdk)

---

## 🎬 Video demostrativo

🔗 [Ver video demostrativo aquí](https://drive.google.com/file/d/1NLMVhFTRbBnXLWcwwliAi2rKvFSVEofA/view?usp=drivesdk)

> El video muestra a todos los integrantes, dura máximo 3 minutos y demuestra las operaciones CRUD completas con validaciones y conexión real a la base de datos.

---

## 📊 Estado final del proyecto

| Criterio | Estado |
|---|---|
| Diseño GUI funcional | ✅ Completo |
| Conexión a base de datos | ✅ Completo |
| Ingreso de registros | ✅ Completo |
| Visualización de registros | ✅ Completo |
| Actualización de registros | ✅ Completo |
| Eliminación de registros | ✅ Completo |
| Validación de campos | ✅ Completo |
| Organización del código | ✅ Completo |
| README.md | ✅ Completo |
| Video demostrativo | ⏳ Pendiente de grabación |
