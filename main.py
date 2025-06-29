from registros import registrar_entrada, registrar_salida, mostrar_miembros_dentro,cargar_dentro
from miembro import Miembro


def menu():
    print("****** Bienvenido al Menú *******")
    print("*********************************")
    print("\t1. Registrar entrada")
    print("\t2. Registrar salida")
    print("\t3. Ver lista de miembros dentro")
    print("\t4. Salir")
    print("*********************************")
    print("*********************************")

cargar_dentro()


while True:
    menu()
    opcion = input("Elije una opcion: ")

    if opcion == "1":
        print("Registrar entrada")
        registrar_entrada()
    elif opcion == "2":
        print("Registrar salida")
        registrar_salida()
    elif opcion == "3":
        print("Ver lista de miembros dentro")
        mostrar_miembros_dentro()
    elif opcion == "4":
        print("Hasta Luego !!! ")
        break
    else:
        print("Opcion no valida, elija otra opcion")







"""
print(type(menu()))

sirve para saber el tipo del elemento 
"""
