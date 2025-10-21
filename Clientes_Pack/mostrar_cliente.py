"""Funciones para listar y ver el detalle de los clientes."""

from Clientes_Pack.lista_clientes import clientes
from Clientes_Pack.funciones_aux import (
    ordenar_clientes,
    formatear_estado,
    normalizar_estado,
    clientes_por_estado,
    buscar_indice_por_id,
    obtener_reservas_de_cliente,
    contar_por_estado,
    validar_id,
)
from Reservas_Pack.lista_reservas import reservas
from Paquetes_Pack.lista_paquetes import paquetes


def mostrar_clientes(estado=None, interactivo=True):
    """Muestra la tabla de clientes con opcion de filtro y detalle interactivo."""
    if estado is not None:
        estado = normalizar_estado(estado)
        listado = clientes_por_estado(clientes, estado)
        titulo = f"Clientes ({formatear_estado(estado)})"
    else:
        listado = clientes
        titulo = "Lista de clientes"

    if not listado:
        if estado is None:
            print("\nNo hay clientes cargados.\n")
        else:
            print(f"\nNo hay clientes con estado {estado}.\n")
        return []

    clientes_ordenados = ordenar_clientes(listado, "id")

    encabezado = f"{'ID':<4} | {'Nombre':<22} | {'DNI':<10} | {'Email':<30} | {'Estado':<10}"
    ancho = len(encabezado)

    print(f"\n{titulo:=^{ancho}}")
    print(encabezado)
    print("-" * ancho)

    for cliente in clientes_ordenados:
        print(
            f"{cliente['id']:<4} | {cliente['nombre']:<22} | {cliente['dni']:<10} | {cliente['email']:<30} | {formatear_estado(cliente['estado']):<10}"
        )

    if estado is None:
        imprimir_resumen_estados()

    if interactivo and estado is None:
        mostrar_detalle_interactivo()
    return clientes_ordenados


def imprimir_resumen_estados():
    """Imprime un pequeno resumen de clientes por estado."""
    conteo = contar_por_estado(clientes)
    if not conteo:
        return
    print("\nResumen por estado:")
    for estado, cantidad in sorted(conteo.items()):
        print(f"  {formatear_estado(estado)}: {cantidad}")


def mostrar_detalle_interactivo():
    """Permite al usuario seleccionar un cliente y ver el detalle."""
    while True:
        opcion = input("\nIngrese el ID del cliente para ver detalle (0 para volver): ").strip()
        if opcion == "0":
            print("Volviendo al menu de clientes...")
            return
        if not validar_id(opcion):
            print("ID invalido. Debe ser un numero positivo.")
            continue
        mostrar_detalle_cliente(int(opcion))


def mostrar_detalle_cliente(id_cliente):
    """Muestra los datos completos de un cliente y sus reservas asociadas."""
    indice = buscar_indice_por_id(clientes, id_cliente)
    if indice == -1:
        print(f"\nNo se encontro un cliente con ID {id_cliente}.")
        return

    cliente = clientes[indice]

    print("\n" + "=" * 60)
    print(f"DETALLE DEL CLIENTE ID {cliente['id']}")
    print("=" * 60)

    print("Cliente")
    print(f"  Nombre .........: {cliente['nombre']}")
    print(f"  DNI ............: {cliente['dni']}")
    print(f"  Email ..........: {cliente['email']}")
    print(f"  Estado .........: {formatear_estado(cliente['estado'])}")

    reservas_cliente = reservas_del_cliente(id_cliente)
    total_reservas = len(reservas_cliente)
    activas = sum(1 for r in reservas_cliente if r['estado'].lower() == 'activa')
    destinos = sorted({r['destino'] for r in reservas_cliente})

    print("\nResumen de reservas")
    print(f"  Total ..........: {total_reservas}")
    print(f"  Activas ........: {activas}")
    print(f"  Destinos .......: {', '.join(destinos) if destinos else '-'}")

    print("\nReservas asociadas")
    if reservas_cliente:
        idx = 1
        for reserva in reservas_cliente:
            print(f"  #{idx} Reserva ID {reserva['id_reserva']}")
            print(f"     Destino ....: {reserva['destino']}")
            print(f"     Personas ...: {reserva['personas']}")
            print(f"     Estado .....: {reserva['estado']}")
            print(f"     Periodo ....: {reserva['periodo']}")
            idx += 1
    else:
        print("  Ninguna reserva registrada.")


def reservas_del_cliente(id_cliente):
    """Normaliza las reservas asociadas a un cliente."""
    normalizadas = []
    for reserva in reservas:
        if type(reserva) is dict:
            if reserva.get("id_cliente") != id_cliente:
                continue
            paquete = buscar_paquete(reserva.get("id_paquete"))
            destino = reserva.get('destino') or (paquete['destino'] if paquete else "Destino desconocido")
            periodo = (
                f"{paquete['fecha_inicio']} -> {paquete['fecha_fin']}" if paquete else "Periodo no disponible"
            )
            normalizadas.append(
                {
                    "id_reserva": reserva.get("id_reserva"),
                    "destino": destino,
                    "personas": reserva.get("personas", "-"),
                    "estado": formatear_estado(reserva.get("estado", "")),
                    "periodo": periodo,
                }
            )
        elif len(reserva) > 1 and reserva[1] == id_cliente:
            destino = reserva[2] if len(reserva) > 2 else reserva[0]
            paquete = buscar_paquete_por_destino(destino)
            periodo = (
                f"{paquete['fecha_inicio']} -> {paquete['fecha_fin']}" if paquete else "Periodo no disponible"
            )
            normalizadas.append(
                {
                    "id_reserva": reserva[0],
                    "destino": destino,
                    "personas": reserva[3] if len(reserva) > 3 else "-",
                    "estado": "-",
                    "periodo": periodo,
                }
            )
    return normalizadas


def buscar_paquete(id_paquete):
    if id_paquete is None:
        return None
    for paquete in paquetes:
        if paquete["id_paquete"] == id_paquete:
            return paquete
    return None


def buscar_paquete_por_destino(destino):
    for paquete in paquetes:
        if paquete["destino"].lower() == destino.lower():
            return paquete
    return None
