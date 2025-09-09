from Reservas_Pack.lista_reservas import reservas
from Paquetes_Pack.lista_paquetes import paquetes
from Paquetes_Pack.mostrar_paquetes import mostrar_paquetes
from Reservas_Pack.mostrar_reservas import mostrar_reservas
from Reservas_Pack.funciones_aux import busqueda_secuencial_por_posicion
import re


# Función para modificar una reserva existente
def modificar_reserva():
    mostrar_reservas()
    id_modificar_txt = input("\nIngrese el ID de la reserva a modificar: ").strip()
    while re.match(r"^\d+$", id_modificar_txt) is None:
        print("\nEntrada inválida. Debe ser un número entero positivo.\n")
        id_modificar_txt = input("Ingrese el ID de la reserva a modificar: ").strip()

    id_modificar = int(id_modificar_txt)

    opcion = ""

    while opcion != "0":
        print("\n\n=== MENÚ MODIFICAR RESERVA ===")
        print("1. Modificar cantidad de personas")
        print("2. Modificar tipo de paquete")
        print("3. Modificar paquete")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ")
        print()  # Espacio adicional para separar la salida
        if opcion == "1":
            modificar_cantPersonas(id_modificar)
        elif opcion == "2":
            modificar_paquete(id_modificar)
        elif opcion == "0":
            print("\nVolviendo al menú principal...\n")
        else:
            print("\nOpción inválida.\n")


# Actualiza la cantidad de personas en una reserva y ajusta los cupos del paquete asociado.
def modificar_cantPersonas(id_modificar):
    # Recorre las reservas para encontrar la que coincide con el ID proporcionado
    for reserva in reservas:
        if reserva[0] == id_modificar:
            print(
                f"ID Reserva: {reserva[0]}, Cliente ID: {reserva[1]}, Destino: {reserva[2]}, Cantidad de personas: {reserva[3]}"
            )
            nueva_cantidad = int(input("Ingrese la nueva cantidad de personas: "))
            diferencia = nueva_cantidad - reserva[3]
            # Validar que la nueva cantidad sea válida y no exceda los cupos disponibles
            for paquete in paquetes:
                if paquete[1] == reserva[2]:
                    if paquete[5] >= diferencia:
                        paquete[5] -= diferencia
                        reserva[3] = nueva_cantidad
                        print(f"Reserva ID {id_modificar} modificada con éxito.")
                    else:
                        print("No hay cupos suficientes para aumentar la reserva.")


# Cambia el paquete turístico de una reserva y ajusta los cupos de los paquetes involucrados.
def modificar_paquete(id_modificar):
    # Recorre las reservas para encontrar la que coincide con el ID proporcionado
    for reserva in reservas:
        if reserva[0] == id_modificar:
            print(
                f"ID Reserva: {reserva[0]}, Cliente ID: {reserva[1]}, Destino: {reserva[2]}, Cantidad de personas: {reserva[3]}"
            )
            mostrar_paquetes()
            nuevo_paquete_id = int(input("Ingrese el ID del nuevo paquete: "))
            # Validar que el ID del paquete exista y tenga cupos disponibles
            while busqueda_secuencial_por_posicion(
                paquetes, nuevo_paquete_id, 0
            ) == -1 or any(
                paquete[0] == nuevo_paquete_id and paquete[5] < reserva[3]
                for paquete in paquetes
            ):
                if (
                    busqueda_secuencial_por_posicion(paquetes, nuevo_paquete_id, 0)
                    == -1
                ):
                    print("ID de paquete no encontrado. Por favor, intente nuevamente.")
                else:
                    print(
                        "El paquete seleccionado no tiene cupos disponibles. Por favor, elija otro paquete."
                    )
                nuevo_paquete_id = int(input("Ingrese el ID del nuevo paquete: "))
            # Restaurar los cupos en el paquete anterior
            for paquete in paquetes:
                if paquete[1] == reserva[2]:
                    paquete[5] += reserva[3]
            # Actualizar la reserva con el nuevo paquete
            for paquete in paquetes:
                if paquete[0] == nuevo_paquete_id:
                    reserva[2] = paquete[1]
                    paquete[5] -= reserva[3]
                    print(f"Reserva ID {id_modificar} modificada con éxito.")
                    return
