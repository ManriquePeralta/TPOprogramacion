# importación de funciones de gestión de reservas
from Reservas_Pack.agregar_reserva import agregar_reserva
from Reservas_Pack.mostrar_reservas import mostrar_reserva
from Reservas_Pack.mostrar_reservas import mostrar_detalle
from Reservas_Pack.modificar_reserva import modificar_reserva
from Reservas_Pack.eliminar_reserva import eliminar_reserva
from Reservas_Pack.estadisticas_reserva import estadisticas_reservas
from Reservas_Pack.mostrar_reservas import mostrar_detalle_interactivo

# Función del menú de reservas
def menu_reservas():
    opcion = ""
    # Bucle del menú de reservas
    while opcion != "0":
        print("\n\n=== MENÚ RESERVAS ===")
        print("1. Agregar reserva")
        print("2. Mostrar reservas")
        print("3. Modificar reserva")
        print("4. Eliminar reserva")
        print("5. Estadísticas de reservas")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ")
        print()  # Espacio adicional para separar la salida
        # Procesar la opción seleccionada
        if opcion == "1":
            agregar_reserva()
        elif opcion == "2":
            mostrar_reserva()           
            mostrar_detalle_interactivo()
        elif opcion == "3":
            modificar_reserva()
        elif opcion == "4":
            eliminar_reserva()
        elif opcion == "5":
            estadisticas_reservas()
        elif opcion == "0":
            print("\nVolviendo al menú principal...\n")
        else:
            print("\nOpción inválida.\n")
