# Importaciones necesarias de otros modulos.
from Paquetes_Pack.mostrar_paquetes import mostrar_paquetes
from Clientes_Pack.mostrar_cliente import mostrar_clientes_activos
from Clientes_Pack.funciones_aux import (
    validar_id as validar_id_cliente,
    buscar_indice_por_id,
    normalizar_estado as normalizar_estado_cliente,
    cargar_clientes_desde_archivo,
)
from Reservas_Pack.funciones_aux import (
    reservas,
    guardar_reservas,
    validar_id,
    validar_cantidad_personas,
    generar_nuevo_id,
)
from Paquetes_Pack.funciones_aux import (
    cargar_paquete_desde_archivo,
    guardar_paquete_en_archivo,
)

# Administra la creacion de una nueva reserva con validaciones.
def agregar_reserva():
    
    print("\n\n=== RESERVAR PAQUETE ===")

    # Muestra y carga los clientes disponibles antes de seleccionar uno.
    mostrar_clientes_activos()
    clientes_actuales = cargar_clientes_desde_archivo()
    paquetes = cargar_paquete_desde_archivo()
    if not clientes_actuales:
        print("No hay clientes cargados para realizar reservas.")
        return

    id_cliente_txt = input("\nIngrese el ID del cliente (0 para salir): ").strip()
    if id_cliente_txt == "0":
        print("Operacion cancelada.")
        return

    # Repite la solicitud hasta recibir un ID valido o cancelar.
    while not validar_id_cliente(id_cliente_txt):
        print("ID invalido. Debe ser un numero positivo.")
        id_cliente_txt = input("Ingrese el ID del cliente (0 para salir): ").strip()
        if id_cliente_txt == "0":
            print("Operacion cancelada.")
            return

    id_cliente = int(id_cliente_txt)
    indice_cliente = buscar_indice_por_id(clientes_actuales, id_cliente)
    while indice_cliente == -1 or normalizar_estado_cliente(clientes_actuales[indice_cliente]["estado"]) != "activo":
        if indice_cliente == -1:
            print("No existe un cliente con ese ID.")
        else:
            print("El cliente no esta activo. Seleccione otro cliente.")
        id_cliente_txt = input("Ingrese el ID del cliente (0 para salir): ").strip()
        if id_cliente_txt == "0":
            print("Operacion cancelada.")
            return
        while not validar_id_cliente(id_cliente_txt):
            print("ID invalido. Debe ser un numero positivo.")
            id_cliente_txt = input("Ingrese el ID del cliente (0 para salir): ").strip()
            if id_cliente_txt == "0":
                print("Operacion cancelada.")
                return
        id_cliente = int(id_cliente_txt)
        clientes_actuales = cargar_clientes_desde_archivo()
        indice_cliente = buscar_indice_por_id(clientes_actuales, id_cliente)

    mostrar_paquetes()
    id_paquete_txt = input("\nIngrese el ID del paquete a reservar (0 para salir): ").strip()
    if id_paquete_txt == "0":
        print("Operacion cancelada.")
        return
    # Se asegura de que el ID de paquete ingresado sea valido.
    while not validar_id(id_paquete_txt):
        print("ID invalido. Debe ser un numero positivo.")
        id_paquete_txt = input("Ingrese el ID del paquete a reservar (0 para salir): ").strip()
        if id_paquete_txt == "0":
            print("Operacion cancelada.")
            return
    id_paquete = int(id_paquete_txt)

    paquete = buscar_paquete(paquetes, id_paquete)
    while paquete is None or paquete["cupos"] == 0:
        # Repite la seleccion cuando el paquete no existe o no tiene cupos.
        if paquete is None:
            print("No existe un paquete con ese ID.")
        else:
            print("El paquete no tiene cupos disponibles.")
        id_paquete_txt = input("Ingrese el ID del paquete a reservar (0 para salir): ").strip()
        if id_paquete_txt == "0":
            print("Operacion cancelada.")
            return
        while not validar_id(id_paquete_txt):
            print("ID invalido. Debe ser un numero positivo.")
            id_paquete_txt = input("Ingrese el ID del paquete a reservar (0 para salir): ").strip()
            if id_paquete_txt == "0":
                print("Operacion cancelada.")
                return
        id_paquete = int(id_paquete_txt)
        paquete = buscar_paquete(paquetes, id_paquete)

    cantidad_txt = input("Cantidad de personas: ").strip()
    # Valida que la cantidad sea numerica y mayor a cero.
    while not validar_cantidad_personas(cantidad_txt):
        print("La cantidad debe ser un numero entero mayor a 0.")
        cantidad_txt = input("Cantidad de personas: ").strip()
    personas = int(cantidad_txt)

    while personas > paquete["cupos"]:
        print("La cantidad supera los cupos disponibles.")
        cantidad_txt = input("Cantidad de personas: ").strip()
        while not validar_cantidad_personas(cantidad_txt):
            print("La cantidad debe ser un numero entero mayor a 0.")
            cantidad_txt = input("Cantidad de personas: ").strip()
        personas = int(cantidad_txt)

    # Genera un identificador unico para la nueva reserva.
    nuevo_id = generar_nuevo_id(reservas)
    nueva_reserva = {
        "id_reserva": nuevo_id,
        "id_cliente": id_cliente,
        "id_paquete": id_paquete,
        "destino": paquete["destino"],
        "personas": personas,
        "estado": "activa",
        "precio_unitario": paquete.get("precio"),
    }
    # Agrega la reserva a la lista global y ajusta los cupos disponibles.
    reservas.append(nueva_reserva)
    paquete["cupos"] -= personas
    
    # Guardar cambios en TXT
    guardar_reservas()

    nombre_cliente = clientes_actuales[indice_cliente]["nombre"]
    print(f"Reserva creada con exito. ID: {nuevo_id} (Cliente: {nombre_cliente}).")

    if not guardar_paquete_en_archivo(paquetes):
        print("Advertencia: no se pudieron guardar los cambios en los paquetes.")


def buscar_paquete(paquetes, id_paquete):
    # Busca un paquete por ID dentro del listado provisto.
    for paquete in paquetes:
        if paquete["id_paquete"] == id_paquete:
            return paquete
    return None
