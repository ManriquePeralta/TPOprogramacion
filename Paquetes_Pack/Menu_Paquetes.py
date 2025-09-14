"""
Módulo de menú principal para la gestión de paquetes turísticos.
Permite mostrar, agregar, modificar, eliminar y ver estadísticas de paquetes.
"""

# Importación de funciones y módulos relacionados con paquetes
from Paquetes_Pack.lista_paquetes import paquetes
from Paquetes_Pack.agregar_paquetes import agregar_paquete
from Paquetes_Pack.modificar_paquete import modificar_paquete
from Paquetes_Pack.eliminar_paquete import eliminar_paquete
from Paquetes_Pack.mostrar_paquetes import mostrar_paquetes
from Paquetes_Pack.validaciones_paquete import mostrar_error
from Paquetes_Pack.estadisticas_paquete import estadisticas_paquetes

def menu_paquetes():
    op = ""
    while op != "0":
        print("\n=== MENÚ PAQUETES ===")
        print("1. Mostrar paquetes")
        print("2. Agregar paquete")
        print("3. Modificar paquete")
        print("4. Eliminar paquete")
        print("5. Estadísticas de paquetes")
        print("0. Volver")
        op = input("Opción: ")
        if op == "1":
            mostrar_paquetes()
        # Función que muestra el menú de opciones para la gestión de paquetes
        elif op == "2":
            agregar_paquete()
        elif op == "3":
            modificar_paquete()
        elif op == "4":
            eliminar_paquete()
        elif op == "5":
            estadisticas_paquetes()
        elif op == "0":
            return
        else:
            mostrar_error("Opción inválida.")

