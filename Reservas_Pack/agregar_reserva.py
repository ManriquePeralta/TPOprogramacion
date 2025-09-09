# Importación de funciones para mostrar paquetes y clientes
from Paquetes_Pack.mostrar_paquetes import mostrar_paquetes
from Clientes_Pack.mostrar_cliente import mostrar_clientes

# Importación de la función para buscar posiciones en listas de reservas
from Reservas_Pack.funciones_aux import busqueda_secuencial_por_posicion


# Importación de listas de reservas, paquetes y clientes
from Reservas_Pack.lista_reservas import reservas
from Paquetes_Pack.lista_paquetes import paquetes
from Clientes_Pack.lista_clientes import clientes

import re


# Esta función permite al usuario agregar una nueva reserva, validando la entrada y actualizando los cupos disponibles en el paquete seleccionado.
def agregar_reserva():
    print("\n\n=== RESERVAR PAQUETE ===")

    # Mostrar lista de clientes disponibles
    mostrar_clientes()
    id_cliente_txt = input("\nIngrese su ID de cliente: ").strip()
    while re.match(r"^\d+$", id_cliente_txt) is None:
        print("\nEntrada inválida. Debe ser un número entero positivo.\n")
        id_cliente_txt = input("Ingrese su ID de cliente: ").strip()

    id_cliente = int(id_cliente_txt)

    # Validar que el ID del cliente exista directamente sin doble validación
    while busqueda_secuencial_por_posicion(clientes, id_cliente, 0) == -1:
        print("\nID de cliente no encontrado. Por favor, intente nuevamente.\n")
        id_cliente_txt = input("Ingrese su ID de cliente: ").strip()
        # Validación por expresiones regulares para asegurar que sea un número entero positivo
        while re.match(r"^\d+$", id_cliente_txt) is None:
            print("\nEntrada inválida. Debe ser un número entero positivo.\n")
            id_cliente_txt = input("Ingrese su ID de cliente: ").strip()
        id_cliente = int(id_cliente_txt)

    # Mostrar lista de paquetes disponibles
    mostrar_paquetes()
    id_paquete_txt = input("\nIngrese el ID del paquete a reservar: ").strip()
    while re.match(r"^\d+$", id_paquete_txt) is None:
        print("\nEntrada inválida. Debe ser un número entero positivo.\n")
        id_paquete_txt = input("Ingrese el ID del paquete a reservar: ").strip()

    id_paquete = int(id_paquete_txt)

    # Validar que el ID del paquete exista y tenga cupos disponibles
    while busqueda_secuencial_por_posicion(paquetes, id_paquete, 0) == -1 or any(
        paquete[0] == id_paquete and paquete[5] == 0 for paquete in paquetes
    ):
        if busqueda_secuencial_por_posicion(paquetes, id_paquete, 0) == -1:
            print("\nID de paquete no encontrado. Por favor, intente nuevamente.\n")
        else:
            print(
                "\nEl paquete seleccionado no tiene cupos disponibles. Por favor, elija otro paquete.\n"
            )
        id_paquete_txt = input("Ingrese el ID del paquete a reservar: ").strip()
        while re.match(r"^\d+$", id_paquete_txt) is None:
            print("\nEntrada inválida. Debe ser un número entero positivo.\n")
            id_paquete_txt = input("Ingrese el ID del paquete a reservar: ").strip()
        id_paquete = int(id_paquete_txt)

    # Solicitar la cantidad de personas para la reserva
    cantidad_personas = int(input("Ingrese la cantidad de personas: "))

    # Validar que la cantidad de personas sea válida y no exceda los cupos disponibles
    for paquete in paquetes:
        if paquete[0] == id_paquete:
            while cantidad_personas <= 0 or cantidad_personas > paquete[5]:
                if cantidad_personas > paquete[5]:
                    print(
                        "La cantidad de personas no puede exceder los cupos disponibles. Por favor, intente nuevamente."
                    )
                elif cantidad_personas <= 0:
                    print(
                        "La cantidad de personas debe ser mayor a 0. Por favor, intente nuevamente."
                    )
                cantidad_personas = int(input("Ingrese la cantidad de personas: "))

            # Insertar la nueva reserva en la lista de reservas
            reserva_id = max([reserva[0] for reserva in reservas], default=0) + 1
            reservas.append([reserva_id, id_cliente, paquete[1], cantidad_personas])
            paquete[5] -= cantidad_personas
            print(f"Reserva realizada con éxito. ID de reserva: {reserva_id}")
