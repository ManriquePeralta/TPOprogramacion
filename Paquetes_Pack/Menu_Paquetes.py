"""Menu principal del modulo de paquetes."""
from validaciones_menu import ingresar_numero
from Paquetes_Pack.mostrar_paquetes import mostrar_paquetes, listar_paquetes
from Paquetes_Pack.agregar_paquetes import agregar_paquete
from Paquetes_Pack.modificar_paquete import modificar_paquete
from Paquetes_Pack.eliminar_paquete import eliminar_paquete
from Paquetes_Pack.estadisticas_paquete import estadisticas_paquetes
from Paquetes_Pack.buscar_paquete import buscar_paquete
from Paquetes_Pack.funciones_aux import mostrar_error


def menu_paquetes():  
    while True:
        print("\n=== MENU PAQUETES ===")
        print("1. Mostrar paquetes")
        print("2. Agregar paquete")
        print("3. Modificar paquete")
        print("4. Eliminar paquete")
        print("5. Buscar paquete")
        print("6. Estadisticas")
        print("0. Volver")
    
        opcion = ingresar_numero("Opcion: ",0,6)

        if opcion == 1:
            submenu_mostrar_paquetes()
        elif opcion == 2:
            agregar_paquete()
        elif opcion == 3:
            modificar_paquete()
        elif opcion == 4:
            eliminar_paquete()
        elif opcion == 5:
            buscar_paquete()
        elif opcion == 6:
            estadisticas_paquetes()
        elif opcion == 0:
            print("Volviendo al menu principal...")
            break
        

def submenu_mostrar_paquetes():
    while True:
        print("\n--- Ver paquetes ---")
        print("1. Todos")
        print("2. Sin cupos")
        print("0. Volver")
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            mostrar_paquetes()
        elif opcion == "2":
            listar_paquetes("sin_cupo")
        elif opcion == "0":
            return
        else:
            mostrar_error("Opcion invalida.")
