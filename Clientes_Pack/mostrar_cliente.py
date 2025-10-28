# Funciones para listar y ver el detalle de los clientes.

from Clientes_Pack.funciones_aux import (
    ordenar_clientes,
    formatear_estado,
    clientes_por_estado,
    buscar_indice_por_id,
    cargar_clientes_desde_archivo,
)
from Reservas_Pack.funciones_aux import reservas
from Paquetes_Pack.funciones_aux import (
    cargar_paquete_desde_archivo,
    buscar_indice_por_id as buscar_paquete_por_id,
)

# Muestra todos los clientes con una tabla simple.
def mostrar_clientes():

    # carga los clientes desde el archivo
    clientes = cargar_clientes_desde_archivo()

    # Verifica si hay clientes para mostrar
    if not clientes:
        print("\nNo hay clientes cargados.\n")
        return []
    
    # Ordena y muestra los clientes en formato tabular
    clientes_ordenados = ordenar_clientes(clientes, "id")
    encabezado = f"{'ID':<4} | {'Nombre':<22} | {'DNI':<10} | {'Email':<30} | {'Estado':<10}"
    ancho = len(encabezado)
    print(f"\n{'Lista de clientes':=^{ancho}}")
    print(encabezado)
    print("-" * ancho)

    # Recorre y muestra cada cliente
    for cliente in clientes_ordenados:
        print(
            f"{cliente['id']:<4} | "
            f"{cliente['nombre']:<22} | "
            f"{cliente['dni']:<10} | "
            f"{cliente['email']:<30} | "
            f"{formatear_estado(cliente['estado']):<10}"
        )

    return clientes_ordenados

# Muestra solo los clientes activos.
def mostrar_clientes_activos():

    # carga los clientes desde el archivo
    clientes = cargar_clientes_desde_archivo()

    # Filtra los clientes activos
    activos = clientes_por_estado(clientes, "activo")
    if not activos:
        print("\nNo hay clientes activos cargados.\n")
        return []
    
    # Ordena y muestra los clientes activos
    activos_ordenados = ordenar_clientes(activos, "id")
    encabezado = f"{'ID':<4} | {'Nombre':<22} | {'DNI':<10} | {'Email':<30} | {'Estado':<10}"
    ancho = len(encabezado)
    print(f"\n{'Clientes activos':=^{ancho}}")
    print(encabezado)
    print("-" * ancho)
    
    # Recorre y muestra cada cliente activo
    for cliente in activos_ordenados:
        print(
            f"{cliente['id']:<4} | "
            f"{cliente['nombre']:<22} | "
            f"{cliente['dni']:<10} | "
            f"{cliente['email']:<30} | "
            f"{formatear_estado(cliente['estado']):<10}"
        )

    return activos_ordenados

# Muestra solo los clientes inactivos.
def mostrar_clientes_inactivos():

    # carga los clientes desde el archivo
    clientes = cargar_clientes_desde_archivo()

    # Filtra los clientes inactivos
    inactivos = clientes_por_estado(clientes, "inactivo")
    if not inactivos:
        print("\nNo hay clientes inactivos cargados.\n")
        return []
    
    # Ordena y muestra los clientes inactivos
    inactivos_ordenados = ordenar_clientes(inactivos, "id")
    encabezado = f"{'ID':<4} | {'Nombre':<22} | {'DNI':<10} | {'Email':<30} | {'Estado':<10}"
    ancho = len(encabezado)
    print(f"\n{'Clientes inactivos':=^{ancho}}")
    print(encabezado)
    print("-" * ancho)

    # Recorre y muestra cada cliente inactivo
    for cliente in inactivos_ordenados:
        print(
            f"{cliente['id']:<4} | "
            f"{cliente['nombre']:<22} | "
            f"{cliente['dni']:<10} | "
            f"{cliente['email']:<30} | "
            f"{formatear_estado(cliente['estado']):<10}"
        )

    return inactivos_ordenados

# Muestra el detalle completo de un cliente y sus reservas.
def mostrar_detalle_cliente(id_cliente):

    # carga los clientes desde el archivo
    clientes = cargar_clientes_desde_archivo()

    # Busca el indice del cliente por su ID
    indice = buscar_indice_por_id(clientes, id_cliente)
    if indice == -1:
        print(f"\nNo se encontro un cliente con ID {id_cliente}.")
        return
    
    # Obtiene el cliente y los paquetes
    cliente = clientes[indice]
    paquetes = cargar_paquete_desde_archivo()

    # Muestra el detalle del cliente
    print("\n" + "=" * 60)
    print(f"DETALLE DEL CLIENTE ID {cliente['id']}")
    print("=" * 60)
    print("Cliente")
    print(f"  Nombre .........: {cliente['nombre']}")
    print(f"  DNI ............: {cliente['dni']}")
    print(f"  Email ..........: {cliente['email']}")
    print(f"  Estado .........: {formatear_estado(cliente['estado'])}")

    # Muestra las reservas asociadas
    print("\nReservas asociadas")
    numero_reserva = 1

    # Recorre todas las reservas para encontrar las del cliente
    for reserva in reservas:
        # Verifica si la reserva pertenece al cliente
        if type(reserva) is dict and reserva.get("id_cliente") == id_cliente:
            destino = reserva.get("destino")
            if not destino:
                destino = "Destino no disponible"
                paquete_id = reserva.get("id_paquete")
                indice_paquete = buscar_paquete_por_id(paquetes, paquete_id)
                if indice_paquete != -1:
                    destino = paquetes[indice_paquete].get("destino", destino)
            personas = reserva.get("personas", "-")
            estado_reserva = formatear_estado(reserva.get("estado", ""))
            # Muestra los detalles de la reserva
            print(f"  #{numero_reserva} Reserva ID {reserva.get('id_reserva', '-')}")
            print(f"     Destino ....: {destino}")
            print(f"     Personas ...: {personas}")
            print(f"     Estado .....: {estado_reserva}")
            numero_reserva += 1
        # Verifica si la reserva es una lista y pertenece al cliente
        elif type(reserva) is list and len(reserva) > 1 and reserva[1] == id_cliente:
            destino_lista = reserva[2] if len(reserva) > 2 else "Destino no disponible"
            personas_lista = reserva[3] if len(reserva) > 3 else "-"
            print(f"  #{numero_reserva} Reserva ID {reserva[0]}")
            print(f"     Destino ....: {destino_lista}")
            print(f"     Personas ...: {personas_lista}")
            print("     Estado .....: -")
            numero_reserva += 1

    if numero_reserva == 1:
        print("  No tiene reservas registradas.")
