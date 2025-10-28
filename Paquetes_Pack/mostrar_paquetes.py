# Funciones para listar paquetes y ver detalles de forma sencilla.

from Paquetes_Pack.funciones_aux import (
    ordenar_paquetes,
    paquetes_sin_cupo,
    buscar_indice_por_id,
    mostrar_error,
    cargar_paquete_desde_archivo,
)
from Reservas_Pack.funciones_aux import reservas
from Clientes_Pack.funciones_aux import formatear_estado, cargar_clientes_desde_archivo


def mostrar_paquetes():
    # Muestra todos los paquetes y devuelve la lista ordenada.
    paquetes = cargar_paquete_desde_archivo()
    if not paquetes:
        mostrar_error("No hay paquetes para mostrar.")
        return []

    paquetes_ordenados = ordenar_paquetes(paquetes, "id_paquete")
    # Construye una cabecera alineada para facilitar la lectura.
    encabezado = (
        f"{'ID':<4} | {'Destino':<22} | {'Precio':>10} | "
        f"{'Inicio':<12} | {'Fin':<12} | {'Cupos':>5} | {'Tipo':<10}"
    )
    ancho = len(encabezado)

    print(f"\n{'Lista de paquetes':=^{ancho}}")
    print(encabezado)
    print("-" * ancho)

    for paquete in paquetes_ordenados:
        print(
            f"{paquete['id_paquete']:<4} | "
            f"{paquete['destino']:<22} | "
            f"${paquete['precio']:>9} | "
            f"{paquete['fecha_inicio']:<12} | "
            f"{paquete['fecha_fin']:<12} | "
            f"{paquete['cupos']:>5} | "
            f"{paquete['tipo']:<10}"
        )

    return paquetes_ordenados


def mostrar_paquetes_sin_cupo():
    # Muestra solo los paquetes que no tienen cupos disponibles.
    paquetes = cargar_paquete_desde_archivo()
    sin_cupo = paquetes_sin_cupo(paquetes)
    if not sin_cupo:
        mostrar_error("No hay paquetes sin cupos disponibles.")
        return []

    # Reutiliza el mismo formato de cabecera que la lista completa.
    encabezado = (
        f"{'ID':<4} | {'Destino':<22} | {'Precio':>10} | "
        f"{'Inicio':<12} | {'Fin':<12} | {'Cupos':>5} | {'Tipo':<10}"
    )
    ancho = len(encabezado)

    print(f"\n{'Paquetes sin cupo':=^{ancho}}")
    print(encabezado)
    print("-" * ancho)
   
    # Muestra los paquetes sin cupo ordenados por ID.
    for paquete in ordenar_paquetes(sin_cupo, "id_paquete"):
        print(
            f"{paquete['id_paquete']:<4} | "
            f"{paquete['destino']:<22} | "
            f"${paquete['precio']:>9} | "
            f"{paquete['fecha_inicio']:<12} | "
            f"{paquete['fecha_fin']:<12} | "
            f"{paquete['cupos']:>5} | "
            f"{paquete['tipo']:<10}"
        )

    return sin_cupo


def mostrar_detalle_paquete(id_paquete):
    # Muestra los datos completos de un paquete y sus relaciones.
    paquetes = cargar_paquete_desde_archivo()
    indice = buscar_indice_por_id(paquetes, id_paquete)
    if indice == -1:
        mostrar_error("No se encontro un paquete con ese ID.")
        return

    paquete = paquetes[indice]

    # Presenta la informacion principal del paquete.
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
        # Muestra todas las reservas que apuntan al paquete.
        for posicion, reserva in enumerate(reservas_asociadas, start=1):
            print(f"  #{posicion} Reserva ID {reserva['id_reserva']}")
            print(f"     Cliente ID : {reserva['id_cliente']}")
            print(f"     Personas   : {reserva['personas']}")
            print(f"     Estado     : {reserva['estado']}")
    else:
        print("  Ninguna reserva registrada.")

    print("\nClientes asociados")
    if clientes_asociados:
        # Resume la informacion de los clientes vinculados.
        for posicion, cliente in enumerate(clientes_asociados, start=1):
            print(f"  #{posicion} {cliente['nombre']} (ID {cliente['id']})")
            print(f"     DNI ......: {cliente['dni']}")
            print(f"     Email ....: {cliente['email']}")
            print(f"     Estado ...: {cliente['estado']}")
            print(f"     Reservas .: {cliente['reservas']}")
    else:
        print("  Ningun cliente vinculado.")


def reservas_del_paquete(id_paquete):
    # Devuelve reservas normalizadas asociadas al paquete.
    normalizadas = []
    # Analiza cada reserva segun su estructura interna.
    for reserva in reservas:
        if type(reserva) is dict and reserva.get("id_paquete") == id_paquete:
            normalizadas.append(
                {
                    "id_reserva": reserva.get("id_reserva"),
                    "id_cliente": reserva.get("id_cliente"),
                    "personas": reserva.get("personas"),
                    "estado": formatear_estado(reserva.get("estado", "")),
                }
            )
        elif type(reserva) is list and len(reserva) > 2 and reserva[2] == id_paquete:
            # Convierte listas en estructuras con claves mas descriptivas.
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
    # Agrupa los clientes vinculados a partir de las reservas normalizadas.
    clientes = cargar_clientes_desde_archivo()
    resumen = []

    for reserva in reservas_asociadas:
        cliente_id = reserva.get("id_cliente")
        if cliente_id is None:
            continue

        # Reutiliza los datos ya recopilados para evitar duplicados.
        encontrado = next((cliente for cliente in resumen if cliente["id"] == cliente_id), None)
        if encontrado is None:
            cliente_datos = next((datos for datos in clientes if datos.get("id") == cliente_id), None)
            if cliente_datos is None:
                continue
            encontrado = {
                "id": cliente_datos["id"],
                "nombre": cliente_datos["nombre"],
                "dni": cliente_datos["dni"],
                "email": cliente_datos["email"],
                "estado": formatear_estado(cliente_datos["estado"]),
                "reservas": 0,
            }
            resumen.append(encontrado)

        encontrado["reservas"] += 1

    return resumen
