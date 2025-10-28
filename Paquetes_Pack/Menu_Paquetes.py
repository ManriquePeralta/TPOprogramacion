# Menu principal del modulo de paquetes.
from validaciones_menu import ingresar_numero
from Paquetes_Pack.mostrar_paquetes import (
    mostrar_paquetes,
    mostrar_paquetes_sin_cupo,
    mostrar_detalle_paquete,
)
from Paquetes_Pack.agregar_paquetes import agregar_paquete
from Paquetes_Pack.modificar_paquete import modificar_paquete
from Paquetes_Pack.eliminar_paquete import eliminar_paquete
from Paquetes_Pack.estadisticas_paquete import estadisticas_paquetes
from Paquetes_Pack.buscar_paquete import buscar_paquete
from Paquetes_Pack.funciones_aux import mostrar_error


def menu_paquetes():  
    # Gestiona las opciones principales del modulo de paquetes.
    while True:
        print("\n=== MENU PAQUETES ===")
        print("1. Mostrar paquetes")
        print("2. Agregar paquete")
        print("3. Modificar paquete")
        print("4. Eliminar paquete")
        print("5. Buscar paquete")
        print("6. Estadisticas")
        print("0. Volver")
    
        # Solicita y valida la opcion elegida por el usuario.
        opcion = ingresar_numero("Opcion: ",0,6)

        # Ejecuta la accion asociada a cada opcion del menu principal.
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
    # Muestra paquetes segun filtros simples y permite ver detalles.
    while True:
        print("\n--- Ver paquetes ---")
        print("1. Todos")
        print("2. Sin cupos")
        print("0. Volver")
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            listado = mostrar_paquetes()
            # Habilita la consulta detallada de un paquete mostrado.
            if listado:
                id_paquete = input("Ingrese el ID del paquete para ver detalle (0 para salir): ").strip()
                while id_paquete not in ("0", ""):
                    if id_paquete.isdigit():
                        mostrar_detalle_paquete(int(id_paquete))
                        break
                    mostrar_error("ID invalido.")
                    id_paquete = input("Ingrese el ID del paquete para ver detalle (0 para salir): ").strip()
        elif opcion == "2":
            # Lista exclusivamente los paquetes sin disponibilidad.
            mostrar_paquetes_sin_cupo()
        elif opcion == "0":
            return
        else:
            # Informa cuando la opcion ingresada es invalida.
            mostrar_error("Opcion invalida.")
