# Funciones para listar reservas y mostrar sus detalles.

from Reservas_Pack.funciones_aux import (
    reservas,
    ordenar_reservas,
    reservas_por_estado,
    contar_por_estado,
    validar_id,
    obtener_reserva_por_id,
    formatear_estado,
)
from Clientes_Pack.funciones_aux import (
    buscar_indice_por_id as buscar_cliente_por_id,
    formatear_estado as formatear_estado_cliente,
    cargar_clientes_desde_archivo,
)
from Paquetes_Pack.funciones_aux import (
    cargar_paquete_desde_archivo,
    buscar_indice_por_id as buscar_paquete_por_id,
)


def mostrar_reservas(estado=None, interactivo=True):
    # Muestra las reservas con opcion de filtro por estado.
    if estado:
        listado = reservas_por_estado(reservas, estado)
        titulo = f"Reservas ({formatear_estado(estado)})"
    else:
        listado = reservas
        titulo = "Lista de reservas"

    if not listado:
        mensaje = "No hay reservas registradas." if estado is None else f"No hay reservas con estado {estado}."
        print(f"\n{mensaje}\n")
        return []

    reservas_ordenadas = ordenar_reservas(listado)
    encabezado = f"{'ID':<4} | {'Cliente':<18} | {'Destino':<24} | {'Personas':<8} | {'Estado':<10}"
    ancho = len(encabezado)

    print(f"\n{titulo:=^{ancho}}")
    print(encabezado)
    print("-" * ancho)

    clientes_actuales = cargar_clientes_desde_archivo()
    paquetes = cargar_paquete_desde_archivo()

    # Recorre la lista ordenada e imprime cada registro con informacion asociada.
    for reserva in reservas_ordenadas:
        indice_cliente = buscar_cliente_por_id(clientes_actuales, reserva["id_cliente"])
        cliente = clientes_actuales[indice_cliente] if indice_cliente != -1 else None
        paquete = obtener_paquete(paquetes, reserva["id_paquete"])
        nombre_cliente = cliente["nombre"] if cliente else "Desconocido"
        destino = reserva.get("destino") or (paquete["destino"] if paquete else "Sin datos")
        print(
            f"{reserva['id_reserva']:<4} | {nombre_cliente:<18} | {destino:<24} | {reserva['personas']:<8} | {formatear_estado(reserva['estado']):<10}"
        )

    if estado is None:
        imprimir_resumen_estados()

    if interactivo and estado is None:
        mostrar_detalle_interactivo()

    return reservas_ordenadas


def imprimir_resumen_estados():
    # Muestra un pequeno resumen por estado.
    conteo = contar_por_estado(reservas)
    if not conteo:
        return
    print("\nResumen por estado:")
    # Ordena alfabeticamente para mantener la salida consistente.
    for estado, cantidad in sorted(conteo.items()):
        print(f"  {formatear_estado(estado)}: {cantidad}")


def mostrar_detalle_interactivo():
    # Permite seleccionar una reserva y ver el detalle.
    while True:
        opcion = input("\nIngrese el ID de la reserva para ver detalle (0 para volver): ").strip()
        if opcion == "0":
            print("Volviendo al menu de reservas...")
            return
        if not validar_id(opcion):
            print("ID invalido. Debe ser un numero positivo.")
            continue
        # Muestra el detalle cuando el ID es valido.
        mostrar_detalle_reserva(int(opcion))


def mostrar_detalle_reserva(id_reserva):
    # Muestra la informacion completa de una reserva.
    reserva = obtener_reserva_por_id(reservas, id_reserva)
    if reserva is None:
        print(f"\nNo se encontro una reserva con ID {id_reserva}.")
        return

    cliente = obtener_cliente(reserva["id_cliente"])
    paquetes = cargar_paquete_desde_archivo()
    paquete = obtener_paquete(paquetes, reserva["id_paquete"])
    destino_reserva = reserva.get("destino") or (paquete["destino"] if paquete else "Sin datos")

    print("\n" + "=" * 60)
    print(f"DETALLE DE LA RESERVA ID {reserva['id_reserva']}")
    print("=" * 60)

    print("Reserva")
    print(f"  Cliente ID .....: {reserva['id_cliente']}")
    print(f"  Paquete ID .....: {reserva['id_paquete']}")
    print(f"  Destino ........: {destino_reserva}")
    print(f"  Personas .......: {reserva['personas']}")
    print(f"  Estado .........: {formatear_estado(reserva['estado'])}")

    precio_unitario = reserva.get('precio_unitario')
    if precio_unitario is None and paquete:
        precio_unitario = paquete.get('precio')
    if precio_unitario is None:
        precio_total = None
    else:
        precio_unitario = float(precio_unitario)
        precio_total = precio_unitario * int(reserva.get('personas', 0))

    print("\nResumen economico")
    if precio_total is None:
        print("  No disponible (paquete eliminado).")
    else:
        print(f"  Precio unitario : ${precio_unitario:.2f}")
        print(f"  Precio estimado : ${precio_total:.2f}")

    print("\nCliente asociado")
    if cliente:
        # Muestra los datos actuales del cliente vinculado.
        print(f"  Nombre .........: {cliente['nombre']}")
        print(f"  DNI ............: {cliente['dni']}")
        print(f"  Email ..........: {cliente['email']}")
        print(f"  Estado .........: {formatear_estado_cliente(cliente['estado'])}")
    else:
        print("  No se encontro informacion del cliente.")

    print("\nPaquete asociado")
    if paquete:
        print(f"  Destino ........: {paquete['destino']}")
        print(f"  Tipo ...........: {paquete['tipo']}")
        print(f"  Precio .........: ${paquete['precio']}")
        print(f"  Fechas .........: {paquete['fecha_inicio']} -> {paquete['fecha_fin']}")
        print(f"  Cupos restantes : {paquete['cupos']}")
    else:
        print("  Paquete no registrado.")


def obtener_cliente(id_cliente):
    # Recupera el cliente asociado a la reserva si esta registrado.
    clientes = cargar_clientes_desde_archivo()
    indice = buscar_cliente_por_id(clientes, id_cliente)
    if indice == -1:
        return None
    return clientes[indice]


def obtener_paquete(paquetes, id_paquete):
    # Busca el paquete correspondiente dentro del listado en memoria.
    indice = buscar_paquete_por_id(paquetes, id_paquete)
    if indice == -1:
        return None
    return paquetes[indice]
    return None


# Alias para compatibilidad con codigo existente
mostrar_reserva = mostrar_reservas
mostrar_detalle = mostrar_detalle_reserva
