from miembro import Miembro
import json


# Lista de folios dentro del gimnasio
dentro = []

def guardar_dentro(archivo="dentro.json"):
    with open(archivo, "w") as f:
        json.dump(dentro, f)

def cargar_dentro(archivo="dentro.json"):
    global dentro
    try:
        with open(archivo, "r") as f:
            dentro = json.load(f)
    except FileNotFoundError:
        dentro = []

# Lista de folios que están dentro del gimnasio ahora mismo

def registrar_entrada():
    folio = input("Ingresa tu folio: ").upper().strip()
    datos = Miembro.obtener_miembro(folio)

    if datos and datos["estatus"] == "activo":
        if folio not in dentro:
            dentro.append(folio)
            guardar_dentro()  # <-- Guarda cambios aquí
            print(f"{datos['nombre']} ha registrado su entrada.")
        else:
            print("Ya estás registrado dentro.")
    else:
        print("Folio no válido o inactivo.")

def registrar_salida():
    folio = input("Ingresa tu folio: ").upper().strip()

    if folio in dentro:
        dentro.remove(folio)
        guardar_dentro()  # <-- Guarda cambios aquí
        print("Hasta luego !!!")
    else:
        print("No estás registrado dentro.")



def mostrar_miembros_dentro():
    if not dentro:
        print("No hay miembros dentro del gimnasio.")
    else:
        print("Miembros dentro:")
        for folio in dentro:
            datos = Miembro.obtener_miembro(folio)
            if datos:
                print(f"- {datos['nombre']} (Folio: {folio})")





