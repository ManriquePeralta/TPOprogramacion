"""Funciones para listar paquetes y mostrar sus detalles."""

from Paquetes_Pack.lista_paquetes import paquetes
from Paquetes_Pack.funciones_aux import (
    ordenar_paquetes,
    paquetes_sin_cupo,
    conteo_por_tipo,
    buscar_indice_por_id,
    mostrar_error,
)
from Reservas_Pack.lista_reservas import reservas
from Clientes_Pack.lista_clientes import clientes
from Clientes_Pack.funciones_aux import formatear_estado


def listar_paquetes(filtro="todos"):
    """Muestra los paquetes aplicando filtros y devuelve el listado ordenado."""
    filtro = filtro.lower()
    if filtro == "sin_cupo":
        listado = paquetes_sin_cupo(paquetes)
        titulo = "Paquetes sin cupos"
    else:
        listado = paquetes
        titulo = "Lista de paquetes"

    if not listado:
        mostrar_error("No hay paquetes para mostrar.")
        return []

    ordenados = ordenar_paquetes(listado)
    encabezado = (
        f"{'ID':<4} | {'Destino':<20} | {'Precio':>10} | "
        f"{'Inicio':<12} | {'Fin':<12} | {'Cupos':>5} | {'Tipo':<10}"
    )
    ancho = len(encabezado)

    print(f"{titulo:=^{ancho}}")
    print(encabezado)
    print("-" * ancho)

    for paquete in ordenados:
        print(
            f"{paquete['id_paquete']:<4} | "
            f"{paquete['destino']:<20} | "
            f"${paquete['precio']:>9} | "
            f"{paquete['fecha_inicio']:<12} | "
            f"{paquete['fecha_fin']:<12} | "
            f"{paquete['cupos']:>5} | "
            f"{paquete['tipo']:<10}"
        )

    if filtro == "todos":
        imprimir_resumen()

    return ordenados


def mostrar_paquetes(filtro="todos"):
    """Muestra paquetes y permite navegar por el detalle."""
    ordenados = listar_paquetes(filtro)
    if filtro == "todos" and ordenados:
        mostrar_detalle_interactivo()
    return ordenados


def imprimir_resumen():
    conteo = conteo_por_tipo(paquetes)
    if not conteo:
        return
    print("\nResumen por tipo:")
    for tipo, cantidad in sorted(conteo.items()):
        print(f"  {tipo}: {cantidad}")


def mostrar_detalle_interactivo():
    while True:
        opcion = input("\nIngrese el ID del paquete para ver detalle (0 para volver): ").strip()
        if opcion == "0":
            print("Volviendo al menu de paquetes...")
            return
        if not opcion.isdigit():
            mostrar_error("El ID debe ser numerico y positivo.")
            continue
        mostrar_detalle_paquete(int(opcion))


def mostrar_detalle_paquete(id_paquete):
    indice = buscar_indice_por_id(paquetes, id_paquete)
    if indice == -1:
        mostrar_error("No se encontro un paquete con ese ID.")
        return

    paquete = paquetes[indice]

    print("\n" + "=" * 60)
    print(f"DETALLE DEL PAQUETE ID {paquete['id_paquete']}")
    print("=" * 60)

    print("Paquete")
    print(f"  Destino .......: {paquete['destino']}")
    print(f"  Tipo ..........: {paquete['tipo']}")
    print(f"  Precio ........: ${paquete['precio']}")
    print(f"  Cupos .........: {paquete['cupos']}")
    print(f"  Fecha inicio ..: {paquete['fecha_inicio']}")
    print(f"  Fecha fin .....: {paquete['fecha_fin']}")
    print(f"  Descripcion ...: {paquete['descripcion']}")

    reservas_asociadas = reservas_del_paquete(id_paquete)
    clientes_asociados = clientes_del_paquete(reservas_asociadas)

    print("\nReservas asociadas")
    if reservas_asociadas:
        idx = 1
        for reserva in reservas_asociadas:
            print(f"  #{idx} Reserva ID {reserva['id_reserva']}")
            print(f"     Cliente ID : {reserva['id_cliente']}")
            print(f"     Personas   : {reserva['personas']}")
            print(f"     Estado     : {reserva['estado']}")
            idx += 1
    else:
        print("  Ninguna reserva registrada.")

    print("\nClientes asociados")
    if clientes_asociados:
        idx = 1
        for cliente in clientes_asociados:
            print(f"  #{idx} {cliente['nombre']} (ID {cliente['id']})")
            print(f"     DNI ......: {cliente['dni']}")
            print(f"     Email ....: {cliente['email']}")
            print(f"     Estado ...: {cliente['estado']}")
            print(f"     Reservas .: {cliente['reservas']}")
            idx += 1
    else:
        print("  Ningun cliente vinculado.")


def reservas_del_paquete(id_paquete):
    """Devuelve reservas normalizadas asociadas al paquete."""
    normalizadas = []
    for reserva in reservas:
        if type(reserva) is dict:
            if reserva.get("id_paquete") != id_paquete:
                continue
            normalizadas.append(
                {
                    "id_reserva": reserva.get("id_reserva"),
                    "id_cliente": reserva.get("id_cliente"),
                    "personas": reserva.get("personas"),
                    "estado": formatear_estado(reserva.get("estado", "")),
                }
            )
        elif len(reserva) > 2 and reserva[2] == id_paquete:
            normalizadas.append(
                {
                    "id_reserva": reserva[0],
                    "id_cliente": reserva[1],
                    "personas": reserva[3] if len(reserva) > 3 else "-",
                    "estado": "-",
                }
            )
    return normalizadas


def clientes_del_paquete(reservas_asociadas):
    """Agrupa los clientes vinculados a partir de las reservas normalizadas."""
    resumen = {}
    for reserva in reservas_asociadas:
        cliente_id = reserva.get("id_cliente")
        if cliente_id is None:
            continue
        if cliente_id not in resumen:
            cliente = next((c for c in clientes if c.get("id") == cliente_id), None)
            if not cliente:
                continue
            resumen[cliente_id] = {
                "id": cliente["id"],
                "nombre": cliente["nombre"],
                "dni": cliente["dni"],
                "email": cliente["email"],
                "estado": formatear_estado(cliente["estado"]),
                "reservas": 0,
            }
        resumen[cliente_id]["reservas"] += 1
    return list(resumen.values())
