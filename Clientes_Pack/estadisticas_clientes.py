"""Estadisticas y reportes para el modulo de clientes."""

from Clientes_Pack.lista_clientes import clientes
from Clientes_Pack.funciones_aux import (
    formatear_estado,
    resumen_estados,
    buscar_indice_por_id,
)
from Reservas_Pack.lista_reservas import reservas


def estadisticas_clientes():
    if not clientes:
        print("\nNo hay clientes cargados para mostrar estadisticas.\n")
        return

    total, activos, inactivos, otros = resumen_estados(clientes)
    conteo_reservas = reservas_por_cliente()
    total_reservas = sum(conteo_reservas.values())
    promedio_reservas = total_reservas / total if total else 0

    print("\n=== ESTADISTICAS DE CLIENTES ===")
    print("Clientes")
    print(f"  Total ..........: {total}")
    print(f"  Activos ........: {activos}")
    print(f"  Inactivos ......: {inactivos}")
    print(f"  Otros estados ..: {otros}")

    print("\nReservas")
    print(f"  Total ..........: {total_reservas}")
    print(f"  Promedio por cliente: {promedio_reservas:.2f}")

    if conteo_reservas:
        top_id = max(conteo_reservas, key=conteo_reservas.get)
        indice = buscar_indice_por_id(clientes, top_id)
        if indice != -1:
            cliente_top = clientes[indice]
            print(
                f"  Mayor actividad : {cliente_top['nombre']} (ID {cliente_top['id']}) "
                f"con {conteo_reservas[top_id]} reservas"
            )

    clientes_sin_reserva = [c for c in clientes if c['id'] not in conteo_reservas]
    print("\nClientes sin reservas")
    if clientes_sin_reserva:
        for cliente in clientes_sin_reserva:
            print(f"  - {cliente['nombre']} ({formatear_estado(cliente['estado'])})")
    else:
        print("  Todos los clientes tienen al menos una reserva.")

    print("\nResumen por estado")
    print(
        "  (Total, Activos, Inactivos, Otros) ="
        f" ({total}, {activos}, {inactivos}, {otros})"
    )


def reservas_por_cliente():
    conteo = {}
    for reserva in reservas:
        if type(reserva) is dict:
            id_cliente = reserva.get("id_cliente")
        elif len(reserva) > 1:
            id_cliente = reserva[1]
        else:
            continue
        conteo[id_cliente] = conteo.get(id_cliente, 0) + 1
    return conteo
