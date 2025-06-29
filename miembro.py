class Miembro:
    # Base de datos simulada de miembros con folio y nombre
    miembros = {
        "F001": {"nombre": "Carlos", "estatus": "activo"},
        "F002": {"nombre": "Ana", "estatus": "activo"},
        "F003": {"nombre": "Luis", "estatus": "inactivo"},
    }

    @classmethod
    def obtener_miembro(cls, folio): # Funciona como intermediario entre las demas partes del codigo, solo sirve en su clase
        return cls.miembros.get(folio)






