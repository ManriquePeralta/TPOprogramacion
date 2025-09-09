# Importación de listas de reservas y paquetes
from Reservas_Pack.lista_reservas import reservas
from Paquetes_Pack.lista_paquetes import paquetes

# Importación de la función para mostrar reservas
from Reservas_Pack.mostrar_reservas import mostrar_reservas
from Reservas_Pack.funciones_aux import busqueda_secuencial_por_posicion
import re


# Esta función elimina una reserva identificada por su ID y restaura los cupos del paquete asociado.
def eliminar_reserva():
    print("\n\n=== ELIMINAR RESERVA ===")
    # Muestra las reservas existentes
    mostrar_reservas()
    id_reserva_txt = input("\nIngrese el ID de la reserva a eliminar: ").strip()
    while re.match(r"^\d+$", id_reserva_txt) is None:
        print("\nEntrada inválida. Debe ser un número entero positivo.\n")
        id_reserva_txt = input("Ingrese el ID de la reserva a eliminar: ").strip()

    id_reserva = int(id_reserva_txt)

    # Validar que el ID de la reserva exista
    while busqueda_secuencial_por_posicion(reservas, id_reserva, 0) == -1:
        print("\nID de reserva no encontrado. Por favor, intente nuevamente.\n")
        id_reserva_txt = input("Ingrese su ID de reserva: ").strip()
        while re.match(r"^\d+$", id_reserva_txt) is None:
            print("\nEntrada inválida. Debe ser un número entero positivo.\n")
            id_reserva_txt = input("Ingrese su ID de reserva: ").strip()
        id_reserva = int(id_reserva_txt)

    # Buscar y eliminar la reserva
    for reserva in reservas:
        if reserva[0] == id_reserva:
            reservas.remove(reserva)
            # Restaurar los cupos en el paquete correspondiente
            for paquete in paquetes:
                if paquete[1] == reserva[2]:
                    paquete[5] += reserva[3]
            print(f"\nReserva ID {id_reserva} eliminada con éxito.\n")
            return

    print(f"\nNo se encontró una reserva con ID {id_reserva}.\n")
