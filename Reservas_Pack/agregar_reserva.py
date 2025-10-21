"""Alta de reservas con validaciones y actualizacion de cupos."""

from Paquetes_Pack.mostrar_paquetes import listar_paquetes
from Clientes_Pack.mostrar_cliente import mostrar_clientes
from Clientes_Pack.funciones_aux import (
    validar_id as validar_id_cliente,
    buscar_indice_por_id,
    normalizar_estado as normalizar_estado_cliente,
)
from Reservas_Pack.funciones_aux import (
    validar_id,
    validar_cantidad_personas,
    generar_nuevo_id,
)
from Reservas_Pack.lista_reservas import reservas
from Paquetes_Pack.lista_paquetes import paquetes
from Clientes_Pack.lista_clientes import clientes


def agregar_reserva():
    print("\n\n=== RESERVAR PAQUETE ===")

    mostrar_clientes("activo", interactivo=False)
    id_cliente_txt = input("\nIngrese el ID del cliente (0 para salir): ").strip()
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
    indice_cliente = buscar_indice_por_id(clientes, id_cliente)
    while indice_cliente == -1 or normalizar_estado_cliente(clientes[indice_cliente]["estado"]) != "activo":
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
        indice_cliente = buscar_indice_por_id(clientes, id_cliente)

    listar_paquetes()
    id_paquete_txt = input("\nIngrese el ID del paquete a reservar (0 para salir): ").strip()
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

    paquete = buscar_paquete(id_paquete)
    while paquete is None or paquete["cupos"] == 0:
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
        paquete = buscar_paquete(id_paquete)

    cantidad_txt = input("Cantidad de personas: ").strip()
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

    nuevo_id = generar_nuevo_id(reservas)
    reservas.append(
        {
            "id_reserva": nuevo_id,
            "id_cliente": id_cliente,
            "id_paquete": id_paquete,
            "destino": paquete["destino"],
            "personas": personas,
            "estado": "activa",
            "precio_unitario": paquete.get("precio"),
        }
    )
    paquete["cupos"] -= personas

    nombre_cliente = clientes[indice_cliente]["nombre"]
    print(f"Reserva creada con exito. ID: {nuevo_id} (Cliente: {nombre_cliente}).")


def buscar_paquete(id_paquete):
    for paquete in paquetes:
        if paquete["id_paquete"] == id_paquete:
            return paquete
    return None
