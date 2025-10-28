# Menu principal del modulo de reservas.
from validaciones_menu import ingresar_numero
from Reservas_Pack.agregar_reserva import agregar_reserva
from Reservas_Pack.mostrar_reservas import mostrar_reservas
from Reservas_Pack.modificar_reserva import modificar_reserva
from Reservas_Pack.eliminar_reserva import eliminar_reserva
from Reservas_Pack.estadisticas_reserva import estadisticas_reservas
from Reservas_Pack.buscar_reserva import buscar_reserva
from Reservas_Pack.funciones_aux import guardar_reservas

def menu_reservas():
    # Coordina las operaciones principales del modulo de reservas.
    while True:
        print("\n=== MENU RESERVAS ===")
        print("1. Mostrar reservas")
        print("2. Agregar reserva")
        print("3. Modificar reserva")
        print("4. Cancelar reserva")
        print("5. Buscar reserva")
        print("6. Estadisticas")
        print("0. Volver al menu principal")

        # Solicita y valida la opcion del usuario dentro del rango permitido.
        opcion = ingresar_numero("Opcion: ",0,6)

        # Enruta la opcion seleccionada hacia la accion correspondiente.
        if opcion == 1:
            submenu_mostrar_reservas()
        elif opcion == 2:
            agregar_reserva()
            guardar_reservas()
        elif opcion == 3:
            modificar_reserva()
            guardar_reservas()
        elif opcion == 4:
            eliminar_reserva()
            guardar_reservas()
        elif opcion == 5:
            buscar_reserva()
        elif opcion == 6:
            estadisticas_reservas()
        elif opcion == 0:
            print("Volviendo al menu principal...")
            break
       

def submenu_mostrar_reservas():
    # Aplica filtros predefinidos y permite revisar reservas.
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
            # Filtra exclusivamente las reservas activas.
            mostrar_reservas("activa")
        elif opcion == "3":
            # Muestra solo las reservas canceladas.
            mostrar_reservas("cancelada")
        elif opcion == "0":
            return
        else:
            # Indica que la opcion ingresada no es valida.
            print("Opcion invalida. Intente nuevamente.")
