import re

def es_nombre_valido(nombre):
    patron = r'^[A-Za-z0-9 .-]+$'
    return re.match(patron, nombre) is not None






