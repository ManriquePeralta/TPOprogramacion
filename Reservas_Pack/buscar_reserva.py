# Buscador de reservas por distintos criterios.

from Reservas_Pack.funciones_aux import (
    reservas,
    validar_id,
    obtener_reserva_por_id,
    reservas_por_cliente,
    reservas_por_estado,
)
from Reservas_Pack.mostrar_reservas import mostrar_detalle_reserva
from Clientes_Pack.funciones_aux import (
    buscar_indice_por_id as buscar_cliente_por_id,
    cargar_clientes_desde_archivo,
)
from Paquetes_Pack.funciones_aux import cargar_paquete_desde_archivo


def buscar_reserva():
    # Gestiona el menu de busqueda para localizar reservas.
    while True:
        print("\n=== BUSCAR RESERVA ===")
        print("1. Por ID de reserva")
        print("2. Por ID de cliente")
        print("3. Por destino")
        print("4. Por estado")
        print("0. Volver")
        opcion = input("Opcion: ").strip()

        if opcion == "0":
            return
        elif opcion == "1":
            # Consulta por un identificador unico de reserva.
            buscar_por_id()
        elif opcion == "2":
            # Muestra todas las reservas asociadas a un cliente.
            buscar_por_cliente()
        elif opcion == "3":
            # Filtra reservas por coincidencia con un destino.
            buscar_por_destino()
        elif opcion == "4":
            # Agrupa reservas segun el estado actual.
            buscar_por_estado()
        else:
            print("Opcion invalida.")


def buscar_por_id():
    # Busca una reserva con un ID especifico y muestra el detalle.
    id_txt = input("Ingrese el ID de la reserva: ").strip()
    if not validar_id(id_txt):
        print("ID invalido. Debe ser numerico positivo.")
        return
    reserva = obtener_reserva_por_id(reservas, int(id_txt))
    if reserva is None:
        print("No se encontro una reserva con ese ID.")
        return
    mostrar_detalle_reserva(reserva["id_reserva"])


def buscar_por_cliente():
    # Reune todas las reservas asociadas a un cliente particular.
    id_txt = input("Ingrese el ID del cliente: ").strip()
    if not validar_id(id_txt):
        print("ID invalido. Debe ser numerico positivo.")
        return
    id_cliente = int(id_txt)
    coincidencias = reservas_por_cliente(reservas, id_cliente)
    if not coincidencias:
        print("El cliente no posee reservas registradas.")
        return

    cliente = obtener_cliente(id_cliente)
    nombre = cliente["nombre"] if cliente else "Desconocido"
    print(f"\nReservas del cliente {nombre}:")
    imprimir_resumen(coincidencias)

    detalle = input("Desea ver el detalle de alguna reserva? Ingrese ID (Enter para omitir): ").strip()
    if detalle:
        if validar_id(detalle):
            # Permite acceder al detalle puntual de la reserva elegida.
            mostrar_detalle_reserva(int(detalle))
        else:
            print("ID invalido. Se omite el detalle.")


def buscar_por_destino():
    # Filtra reservas que coinciden parcialmente con un destino.
    termino = input("Ingrese parte del destino a buscar: ").strip().lower()
    if not termino:
        print("Debe ingresar al menos una letra.")
        return

    coincidencias = []
    paquetes = cargar_paquete_desde_archivo()
    # Busca coincidencias comparando contra el destino del paquete.
    for reserva in reservas:
        paquete = buscar_paquete(paquetes, reserva["id_paquete"])
        destino = paquete["destino"] if paquete else ""
        if termino in destino.lower():
            coincidencias.append(reserva)

    if not coincidencias:
        print("No se encontraron reservas para ese destino.")
        return

    print("\nReservas encontradas:")
    imprimir_resumen(coincidencias)


def buscar_por_estado():
    # Lista reservas segun su estado actual.
    estado = input("Ingrese el estado (Activa/Cancelada): ").strip().lower()
    coincidencias = reservas_por_estado(reservas, estado)
    if not coincidencias:
        print("No hay reservas con ese estado.")
        return
    print(f"\nReservas con estado {estado.capitalize()}:")
    imprimir_resumen(coincidencias)


def imprimir_resumen(listado):
    # Muestra un resumen tabulado de las reservas encontradas.
    encabezado = f"{'ID':<4} | {'Cliente':<18} | {'Destino':<24} | {'Personas':<8} | {'Estado':<10}"
    print(encabezado)
    print("-" * len(encabezado))
    paquetes = cargar_paquete_desde_archivo()
    # Combina informacion de clientes y paquetes para enriquecer el listado.
    for reserva in listado:
        cliente = obtener_cliente(reserva["id_cliente"])
        paquete = buscar_paquete(paquetes, reserva["id_paquete"])
        nombre = cliente["nombre"] if cliente else "Desconocido"
        destino = paquete["destino"] if paquete else "Sin datos"
        print(
            f"{reserva['id_reserva']:<4} | {nombre:<18} | {destino:<24} | {reserva['personas']:<8} | {reserva['estado'].capitalize():<10}"
        )


def obtener_cliente(id_cliente):
    # Devuelve los datos del cliente correspondiente al ID dado.
    clientes = cargar_clientes_desde_archivo()
    indice = buscar_cliente_por_id(clientes, id_cliente)
    if indice == -1:
        return None
    return clientes[indice]


def buscar_paquete(paquetes, id_paquete):
    # Retorna el paquete vinculado al ID indicado o None si no existe.
    for paquete in paquetes:
        if paquete["id_paquete"] == id_paquete:
            return paquete
    return None
