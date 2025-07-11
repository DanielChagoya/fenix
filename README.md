# 🦅 Fénix - Control de Entradas y Salidas
Fénix es una aplicación de escritorio desarrollada en Python con Tkinter para gestionar el control de entradas y salidas de miembros en un gimnasio.
Ideal para pequeños gimnasios que buscan llevar un control básico pero ordenado.
---

## ✨ Características
- 🛂 Registro de entrada y salida de miembros con validación.
- 🗂️ Visualización del historial completo en una ventana aparte con scroll.
- 🎨 Interfaz gráfica clara con colores personalizados.
- 📁 Manejo de registros en archivo CSV (registro_fenix.csv).
- 🧠 Validaciones para evitar registros duplicados y entradas vacías.
- 🧩 Modularización del código para fácil mantenimiento y escalabilidad.

---

## 🛠 Requisitos
- Python 3.x
- Módulo tkinter (viene preinstalado en la mayoría de distribuciones de Python)

---

## 🗂️ Estructura del proyecto

```plaintext
- main.py              # Punto de entrada y configuración de la interfaz.
- registros.py         # Funciones para registrar entradas y salidas.
- historial.py         # Función para mostrar el historial completo.
- vista.py             # Funciones relacionadas con la interfaz gráfica (listas, validaciones).
- estilos.py           # Variables y constantes de colores, fuentes y estilos.
- registro_fenix.csv   # Archivo donde se guardan los registros (inicialmente vacío).
```

## ▶️ Cómo usar
- 📥 Clona o descarga el repositorio.
- 🖥 Ejecuta el archivo main.py con Python.
- ✅ Usa la interfaz para registrar entradas y salidas.
- 📚 Visualiza el historial completo con el botón correspondiente.


```bash
python main.py
```

---


## 📌 Pendiente por implementar

- Interfaz gráfica con Tkinter
- Exportación del historial a Excel o PDF
- Registro por fecha y hora detallada
- Control de membresía activa/inactiva


## 🚀 Próximos pasos
- 🔄 Migrar el almacenamiento de registros a una base de datos (MySQL o SQLite).
- 🧱 Mejorar la interfaz con más funcionalidades y diseño visual.
- 🔍 Añadir búsqueda, filtros y reportes para el historial.


---

## 👨‍💻 Autor
Daniel Chagoya
Desarrollador de Software | Ingeniero en Sistemas Computacionales 

--- 

## 📃 Licencia
Este proyecto está bajo la licencia MIT.
