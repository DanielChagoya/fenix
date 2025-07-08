import tkinter as tk

def ver_registros(miembros):
    miembros.delete(0, tk.END)

    try:
        with open("registro_fenix.csv", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
        for linea in lineas:
            miembros.insert(tk.END, linea.strip())
    except FileNotFoundError:
        miembros.insert(tk.END, "No hay registros aún.")
