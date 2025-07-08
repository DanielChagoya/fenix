import tkinter as tk

def mostrar_historial():
    nw_ventana = tk.Toplevel()
    nw_ventana.configure(bg="#cc0000")
    nw_ventana.title("Historial completo")

    frame_historial = tk.Frame(nw_ventana, bg="#cc0000")
    frame_historial.pack(padx=10, pady=10)

    area_texto = tk.Text(frame_historial, width=60, height=20,
                         bg="#333333", fg="#CCCCCC",
                         font=("Segoe UI", 11, "bold"),
                         bd=0, relief="flat")
    area_texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame_historial, orient=tk.VERTICAL, command=area_texto.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    area_texto.config(yscrollcommand=scrollbar.set)

    try:
        with open("registro_fenix.csv", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            area_texto.insert("1.0", contenido)
    except FileNotFoundError:
        area_texto.insert("1.0", "No se encontró el archivo de historial.")
