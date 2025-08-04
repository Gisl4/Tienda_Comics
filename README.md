# Tienda de Cómics 🚀

¡Bienvenida/o a tu gestor de Tienda de Cómics! Esta aplicación de consola en Python te inspira a llevar tu pasión por los cómics al mundo de la organización tradicional: catálogo, clientes y ventas, todo al alcance de tu teclado.

##  🗂️ Estructura del Proyecto

tienda_comics/
├── data/
│ ├── catalogo.txt # Datos del catálogo de cómics
│ ├── clientes.txt # Registro de clientes
│ └── ventas.txt # Historial de ventas
├── docs/ # Documentación y utilidades futuras
├── models/ # Clases y lógica de negocio
│ ├── cliente.py # Gestión de clientes (datos, validaciones)
│ └── gestion.py # Estructura de cómics, ventas y operaciones básicas
├── services/ # Funciones de alto nivel para la tienda
│ └── tienda.py # Interfaz de la tienda y operaciones de negocio
└── main.py # Punto de entrada: menú principal e interacción con el usuario


## 🎯 Características Principales

- **Gestión de Clientes**: Alta, baja y edición de datos (nombre, edad, email, membresía).  
- **Catálogo de Cómics**: Visualización, búsqueda y mantenimiento del inventario.  
- **Ventas**: Registro de ventas con historial y guardado automático.  
- **Persistencia**: Todos los cambios se guardan en archivos de texto (.txt) para que no pierdas nada.


## ⚙️ Requisitos

- **Python 3.10** o superior (probado en 3.12).  
- Sólo módulos de la biblioteca estándar de Python.

> 💡 *Tip tradicional:* Usa un entorno virtual para aislar dependencias:
> ```bash
> python -m venv venv
> source venv/bin/activate  # Linux/MacOS
> venv\Scripts\activate     # Windows
> ```

## 📥 Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tienda_comics.git
   cd tienda_comics
2 Activa tu entorno virtual (ver sección anterior).
3 ¡Listo! No hay dependencias extras.


## 🚀 Uso
Ejecuta el programa con:

bash
Copiar
Editar
python main.py

Sigue las instrucciones del menú para:

Ver el catálogo de cómics.

Registrar nuevos clientes.

Realizar ventas.

Consultar historial.

⏳ Consejo: Presiona Enter cuando el programa te lo pida para avanzar sin prisa.


## 📄 Licencia
© 2025 Gisell. Todos los derechos reservados.
Este código es de propiedad exclusiva de Gisell. Queda estrictamente prohibida su copia, distribución, modificación o uso comercial sin autorización expresa por escrito.