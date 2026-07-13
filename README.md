# Grupo6_Proyecto_Final_POO_GUI
🏨 Sistema de Gestión de Servicios de Hotel
Proyecto Segundo Parcial — GUI con Base de Datos | CACA | Grupo 6
📋 Descripción general
Aplicación de escritorio desarrollada en Python con PySide6 , conectada a SQL Server , que permite gestionar servicios de un hotel mediante una interfaz gráfica con operaciones CRUD completas: registrar, consultar, actualizar y eliminar registros desde la GUI hacia la base de datos.

👥 Integrantes del grupo
Nombre	Rol
Luna Henry	Integrante
Sánchez Adrián	Integrante
Mercán Evelyn	Integrante
Veintimilla Alejandra	Integrante
Rodríguez Nayeli	Integrante
Jornada: Matutina | Grupo: 6

✅ Funcionalidades implementadas
Operación	Descripción
Guardar (CREAR)	Registra un nuevo servicio en la base de datos con validaciones previas
Mostrar (LEER)	Consulta y muestra todos los registros almacenados en la tabla.
Actualizar (ACTUALIZACIÓN)	Modifica descripción, precio y correo de un servicio existente
Eliminar (DELETE)	Borra un registro con confirmación previa del usuario
Validaciones	Campos obligatorios, precio positivo, correo con regex, código máx. 5 caracteres
🛠️ Tecnologías utilizadas
Python 3.12+
PySide6 — Interfaz gráfica de usuario
pyodbc — Conexión a SQL Server
SQL Server — Base de datos (ODBC Driver 17)
PyCharm : entorno de desarrollo
▶️Instrucciones para ejecutar
Clonar el repositorio:

git clone <url-repositorio>
cd Proyecto_Gestion_de_hotel
Instalar dependencias:

pip install PySide6 pyodbc
Cree la tabla en SQL Server ejecutando el script:

crear_tabla.sql
Ejecutar la aplicación:

python main.py
🗂️ Estructura del proyecto
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
🗄️ Descripción de la base de datos
Servidor: 10.4.107.75
Base de datos: SAP
Tabla: servicios_hotel

Campo	Tipo	Descripción
codigo	VARCHAR(5) PK	Código único del servicio (máx. 5 caracteres)
descripcion	VARCHAR(200)	Descripción del servicio
precio_base	DECIMAL(10,2)	Precio base del servicio
correo	VARCHAR(100)	Correo de contacto del servicio
🔐 Validaciones implementadas
Campo	Validación
Código	No vacío, máximo 5 caracteres (bloqueado en la UI)
Descripción	No vacío, mínimo 5 caracteres
Precio base	No vacío, debe ser número, mayor a cero, menor a 99,999
Correo	Formato válido validado con expresión regularr'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
Duplicados	No permite guardar un código ya existente
Eliminación	Solicita confirmación antes de borrar
Actualización	Verifica que el código existe antes de modificar
📸 Capturas de pantalla
Captura 1
Captura 2
Captura 3
🎬 Video demostrativo
🔗 Ver vídeo demostrativo aquí

El video muestra a todos los integrantes, dura máximo 3 minutos y demuestra las operaciones CRUD completas con validaciones y conexión real a la base de datos.

📊 Estado final del proyecto
Criterio	Estado
Diseño GUI funcional	✅ Completo
Conexión a base de datos	✅ Completo
Ingreso de registros	✅ Completo
Visualización de registros	✅ Completo
Actualización de registros	✅ Completo
Eliminación de registros	✅ Completo
Validación de campos	✅ Completo
Organización del código	✅ Completo
LÉAME.md	✅ Completo
Video demostrativo	⏳ Pendiente de grabación
