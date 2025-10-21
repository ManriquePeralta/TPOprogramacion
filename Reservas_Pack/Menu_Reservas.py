"""Menu principal del modulo de reservas."""
from validaciones_menu import ingresar_numero
from Reservas_Pack.agregar_reserva import agregar_reserva
from Reservas_Pack.mostrar_reservas import mostrar_reservas
from Reservas_Pack.modificar_reserva import modificar_reserva
from Reservas_Pack.eliminar_reserva import eliminar_reserva
from Reservas_Pack.estadisticas_reserva import estadisticas_reservas
from Reservas_Pack.buscar_reserva import buscar_reserva


def menu_reservas():
    while True:
        print("\n=== MENU RESERVAS ===")
        print("1. Mostrar reservas")
        print("2. Agregar reserva")
        print("3. Modificar reserva")
        print("4. Cancelar reserva")
        print("5. Buscar reserva")
        print("6. Estadisticas")
        print("0. Volver al menu principal")

        opcion = ingresar_numero("Opcion: ",0,6)

        if opcion == 1:
            submenu_mostrar_reservas()
        elif opcion == 2:
            agregar_reserva()
        elif opcion == 3:
            modificar_reserva()
        elif opcion == 4:
            eliminar_reserva()
        elif opcion == 5:
            buscar_reserva()
        elif opcion == 6:
            estadisticas_reservas()
        elif opcion == 0:
            print("Volviendo al menu principal...")
            break
       

def submenu_mostrar_reservas():
    while True:
        print("\n--- Ver reservas ---")
        print("1. Todas")
        print("2. Solo activas")
        print("3. Solo canceladas")
        print("0. Volver")
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            mostrar_reservas()
        elif opcion == "2":
            mostrar_reservas("activa")
        elif opcion == "3":
            mostrar_reservas("cancelada")
        elif opcion == "0":
            return
        else:
            print("Opcion invalida. Intente nuevamente.")
