# registros.py

from datetime import datetime
from tkinter import messagebox

def registrar_entrada(nombre):
    nombre = nombre.strip()

    if not nombre:
        messagebox.showwarning("Campo vacío", "Por favor, ingresa un nombre válido.")
        return

    hora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    try:
        with open("registro_fenix.csv", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            if lineas:
                ultima_linea = lineas[-1].strip()
                ultimo_nombre, ultimo_tipo, _ = ultima_linea.split(",", 2)
                if ultimo_nombre == nombre and ultimo_tipo == "entrada":
                    messagebox.showwarning("Registro duplicado", f"{nombre} ya tiene una entrada registrada.")
                    return
    except FileNotFoundError:
        pass  # Si no existe el archivo, se creará más abajo

    with open("registro_fenix.csv", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre},entrada,{hora}\n")

    messagebox.showinfo("Entrada registrada", f"{nombre} ha entrado a las {hora}")

def registrar_salida(nombre):
    nombre = nombre.strip()

    if not nombre:
        messagebox.showwarning("Campo vacío", "Por favor, ingresa un nombre válido.")
        return

    hora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open("registro_fenix.csv", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre},salida,{hora}\n")

    messagebox.showinfo("Salida registrada", f"{nombre} ha salido a las {hora}")
