"""Menu principal del modulo de clientes."""
from validaciones_menu import ingresar_numero
from Clientes_Pack.mostrar_cliente import mostrar_clientes
from Clientes_Pack.agregar_cliente import agregar_cliente
from Clientes_Pack.modificar_cliente import modificar_cliente
from Clientes_Pack.eliminar_cliente import eliminar_cliente
from Clientes_Pack.estadisticas_clientes import estadisticas_clientes
from Clientes_Pack.buscar_cliente import buscar_cliente


def menu_clientes():
    while True:
        print("\n=== MENU CLIENTES ===")
        print("1. Mostrar clientes")
        print("2. Agregar cliente")
        print("3. Modificar cliente")
        print("4. Eliminar cliente (baja logica)")
        print("5. Buscar cliente")
        print("6. Estadisticas de clientes")
        print("0. Volver al menu principal")

        opcion = ingresar_numero("Opcion: ",0,6)

        if opcion == 1:
            submenu_mostrar_clientes()
        elif opcion == 2:
            agregar_cliente()
        elif opcion == 3:
            modificar_cliente()
        elif opcion == 4:
            eliminar_cliente()
        elif opcion == 5:
            buscar_cliente()
        elif opcion == 6:
            estadisticas_clientes()
        elif opcion == 0:
            print("Volviendo al menu principal...")
            break
    

def submenu_mostrar_clientes():
    while True:
        print("\n--- Ver clientes ---")
        print("1. Todos")
        print("2. Solo activos")
        print("3. Solo inactivos")
        print("0. Volver")
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            mostrar_clientes()
        elif opcion == "2":
            mostrar_clientes("activo")
        elif opcion == "3":
            mostrar_clientes("inactivo")
        elif opcion == "0":
            return
        else:
            print("Opcion invalida. Intente nuevamente.")
