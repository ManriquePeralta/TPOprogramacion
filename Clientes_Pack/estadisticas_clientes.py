# importa las todas las funciones necesarias
from Clientes_Pack.funciones_aux import (
    formatear_estado,
    resumen_estados,
    buscar_indice_por_id,
    cargar_clientes_desde_archivo,
)
from Reservas_Pack.funciones_aux import reservas

# Genera y muestra estadisticas sobre los clientes y sus reservas.
def estadisticas_clientes():
    # Carga los clientes desde el archivo
    clientes = cargar_clientes_desde_archivo()
    if not clientes:
        print("\nNo hay clientes cargados para mostrar estadisticas.\n")
        return
    
    # Obtiene el resumen por estado de los clientes
    total, activos, inactivos, otros = resumen_estados(clientes)
    conteo_reservas = reservas_por_cliente()
    total_reservas = 0

    # Calcula el total de reservas realizadas
    for id_cliente_reserva in conteo_reservas:
        total_reservas += conteo_reservas[id_cliente_reserva]
    promedio_reservas = total_reservas / total if total else 0

    # Muestra los resultados
    print("\n=== ESTADISTICAS DE CLIENTES ===")
    print("Clientes")
    print(f"  Total ..........: {total}")
    print(f"  Activos ........: {activos}")
    print(f"  Inactivos ......: {inactivos}")
    print(f"  Otros estados ..: {otros}")

    print("\nReservas")
    print(f"  Total ..........: {total_reservas}")
    print(f"  Promedio por cliente: {promedio_reservas:.2f}")

    # Cliente con mas reservas
    if conteo_reservas:
        top_id = max(conteo_reservas, key=conteo_reservas.get)
        indice = buscar_indice_por_id(clientes, top_id)
        if indice != -1:
            cliente_top = clientes[indice]
            print(
                f"  Mayor actividad : {cliente_top['nombre']} (ID {cliente_top['id']}) "
                f"con {conteo_reservas[top_id]} reservas"
            )
    # Lista de clientes sin reservas
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

# Cuenta las reservas por cliente usando su ID.
def reservas_por_cliente():
    conteo = {}
    # Recorre todas las reservas y cuenta por ID de cliente
    for reserva in reservas:
        if type(reserva) is dict:
            id_cliente = reserva.get("id_cliente")
        elif len(reserva) > 1:
            id_cliente = reserva[1]
        else:
            continue
        conteo[id_cliente] = conteo.get(id_cliente, 0) + 1
    return conteo
