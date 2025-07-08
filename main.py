import tkinter as tk
from registros import registrar_entrada, registrar_salida
from historial import mostrar_historial
from vista import ver_registros
from estilos import *


# Ventana principal
ventana = tk.Tk()
ventana.title("Fénix - Control de Entradas y Salidas")
ventana.configure(bg=COLOR_FONDO)

# Etiqueta
label_nombre = tk.Label(
    ventana,
    text="Nombre o ID del miembro:",
    fg=COLOR_TEXTO,
    bg=COLOR_FONDO,
    font=FUENTE_LABEL
)
label_nombre.pack(pady=5)

# Entrada
entrada_nombre = tk.Entry(
    ventana,
    width=40,
    font=FUENTE_ENTRADA,
    bg=COLOR_ENTRADA_BG,
    fg=COLOR_TEXTO_ENTRY,
    insertbackground=COLOR_CURSOR
)
entrada_nombre.pack(pady=10)

# Botón entrada
btn_entrada = tk.Button(
    ventana,
    text="Registrar Entrada",
    fg="#FFFFFF",
    bg=COLOR_BOTON_ENTRADA,
    activebackground=COLOR_BOTON_ENTRADA_HOVER,
    font=FUENTE_BOTON,
    command=lambda: (
        registrar_entrada(entrada_nombre.get()),
        entrada_nombre.delete(0, tk.END),
        ver_registros()
    )
)
btn_entrada.pack(pady=5)

# Botón salida
btn_salida = tk.Button(
    ventana,
    text="Registrar Salida",
    fg="#000000",
    bg=COLOR_BOTON_SALIDA,
    activebackground=COLOR_BOTON_SALIDA_HOVER,
    font=FUENTE_BOTON,
    command=lambda: (
        registrar_salida(entrada_nombre.get()),
        entrada_nombre.delete(0, tk.END),
        ver_registros()
    )
)
btn_salida.pack(pady=5)


# Frame para lista
frame_lista = tk.Frame(ventana)
frame_lista.pack(pady=10)

# Lista
miembros = tk.Listbox(
    frame_lista,
    width=50,
    height=10,
    bg=COLOR_ENTRADA_BG,
    fg=COLOR_TEXTO,
    font=FUENTE_LISTA
)
miembros.pack(side=tk.LEFT, fill=tk.BOTH)

# Scrollbar
scroll = tk.Scrollbar(frame_lista, orient=tk.VERTICAL, bg=COLOR_SCROLL)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
miembros.config(yscrollcommand=scroll.set)
scroll.config(command=miembros.yview)

# Botón historial
btn_historial = tk.Button(
    ventana,
    text="Mostrar historial",
    fg=COLOR_TEXTO,
    bg=COLOR_SCROLL,
    activebackground=COLOR_SCROLL_HOVER,
    font=FUENTE_BOTON,
    command=mostrar_historial
)
btn_historial.pack(pady=5)

# Cargar registros al iniciar
ver_registros(miembros)

# Loop principal
ventana.mainloop()




