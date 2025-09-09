from Paquetes_Pack.lista_paquetes import paquetes
from Paquetes_Pack.agregar_paquetes import agregar_paquete
from Paquetes_Pack.modificar_paquete import modificar_paquete
from Paquetes_Pack.eliminar_paquete import eliminar_paquete
from Paquetes_Pack.mostrar_paquetes import mostrar_paquetes

def menu_paquetes():
    op = ""
    while op != "0":
        print("\n=== MENÚ PAQUETES ===")
        print("1. Mostrar paquetes")
        print("2. Agregar paquete")
        print("3. Modificar paquete")
        print("4. Eliminar paquete")
        print("0. Volver")
        op = input("Opción: ")
        if op == "1":
            mostrar_paquetes()
        elif op == "2":
            agregar_paquete()
        elif op == "3":
            modificar_paquete()
        elif op == "4":
            eliminar_paquete()
        elif op == "0":
            return
        else:
            print("❌ Opción inválida.")

