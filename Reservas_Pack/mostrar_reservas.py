# Importar funciones auxiliares y listas
from Reservas_Pack.funciones_aux import ordenar_lista, busqueda_secuencial_por_posicion
from Clientes_Pack.lista_clientes import clientes
from Paquetes_Pack.lista_paquetes import paquetes
from Reservas_Pack.lista_reservas import reservas
import re


# Función para mostrar las reservas ordenadas por destino y luego preguntar por el detalle
def mostrar_reserva():
    largo = f'{"ID Reserva":<3} | {"ID Cliente":<3} | {"Destino":<24} | {"Cant. Personas":<3}'
    ancho_total = len(largo)

    print(f'\n\n{" LISTA DE RESERVAS ":=^{ancho_total}}\n')

    if len(reservas) == 0:
        print("No hay reservas registradas.\n")
        return
    else:
        # Ordenar reservas usando la función ordenar_lista
        reservas_ordenados = ordenar_lista(reservas, 0)  # Ordenar por ID de reserva

        # Encabezado
        print(
            f'{"ID Reserva":<3} | {"ID Cliente":<3} | {"Destino":<24} | {"Cant. Personas":<3}'
        )
        print("-" * 67)

        # Filas
        for c in reservas_ordenados:
            print(f"{c[0]:<10} | {c[1]:<10} | {c[2]:<24} | {c[3]}")

def mostrar_detalle(id_reserva):
    id_reserva = int(id_reserva)  # Asegurarse de que el ID sea un entero
    for reserva in reservas:
        if reserva[0] == id_reserva:
            id_cliente = reserva[1]
            destino = reserva[2]
            cant_personas = reserva[3]

            # Obtener datos del cliente
            indice_cliente = busqueda_secuencial_por_posicion(clientes, id_cliente, 0)
            cliente = clientes[indice_cliente] if indice_cliente != -1 else None

            # Obtener datos del paquete
            paquete = next((p for p in paquetes if p["destino"] == destino), None)

            # Mostrar datos relacionados de forma ordenada y visual
            print("\n=== DETALLE DE LA RESERVA ===")
            print(f"Reserva:")
            print(f"  Destino: {destino}")
            print(f"  Cantidad de personas: {cant_personas}")

            print("\nCliente:")
            if cliente:
                print(f"  Nombre: {cliente[1]}")
                print(f"  DNI: {cliente[2]}")
                print(f"  Dirección: {cliente[3]}")
            else:
                print("  Cliente no encontrado.")

            print("\nPaquete:")
            if paquete:
                print(f"  Precio: {paquete['precio']}")
                print(f"  Fecha inicio: {paquete['fecha_inicio']}")
                print(f"  Fecha fin: {paquete['fecha_fin']}")
                print(f"  Cupos disponibles: {paquete['cupos']}")
            else:
                print("  Paquete no encontrado.")

def mostrar_detalle_interactivo():
    while True:
        id_reserva = input("\n\nIngrese el ID de la reserva para ver los detalles (0 para salir): ")
        if id_reserva == "0":
            print("Saliendo del detalle de reservas...")
            return
        mostrar_detalle(id_reserva)
