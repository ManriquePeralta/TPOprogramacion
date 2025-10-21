"""Baja logica de clientes (marcar como inactivos y limpiar reservas)."""

from Clientes_Pack.lista_clientes import clientes
from Clientes_Pack.funciones_aux import (
    validar_id,
    buscar_indice_por_id,
    normalizar_estado,
    formatear_estado
)
from Clientes_Pack.mostrar_cliente import mostrar_clientes
from Reservas_Pack.lista_reservas import reservas
from Reservas_Pack.funciones_aux import normalizar_estado as normalizar_estado_reserva
from Paquetes_Pack.lista_paquetes import paquetes


def eliminar_cliente():
    print("\n=== ELIMINAR CLIENTE ===")
    listado = mostrar_clientes(interactivo=False)
    if not listado:
        return

    id_cliente_txt = input("\nIngrese el ID del cliente a inactivar (0 para salir): ").strip()

    if id_cliente_txt == "0":
        print("Operacion cancelada. No se modifico ningun cliente.")
        return

    while not validar_id(id_cliente_txt):
        print("ID invalido. Debe ser un numero positivo.")
        id_cliente_txt = input("Ingrese el ID del cliente a inactivar (0 para salir): ").strip()
        if id_cliente_txt == "0":
            print("Operacion cancelada. No se modifico ningun cliente.")
            return

    id_cliente = int(id_cliente_txt)
    indice = buscar_indice_por_id(clientes, id_cliente)

    if indice == -1:
        print(f"No se encontro un cliente con ID {id_cliente}.")
        return

    cliente = clientes[indice]
    estado_actual = normalizar_estado(cliente.get("estado", ""))

    if estado_actual == "inactivo":
        print(f"El cliente {cliente['nombre']} ya se encuentra inactivo.")
        return

    confirmar = input(f"Confirma marcar como inactivo a {cliente['nombre']}? (s/n): ").strip().lower()
    while confirmar not in ("s", "n"):
        confirmar = input("Respuesta invalida. Confirma marcar como inactivo? (s/n): ").strip().lower()

    if confirmar == "n":
        print("Operacion cancelada por el usuario.")
        return

    cliente["estado"] = "inactivo"

    canceladas = 0
    for indice, reserva in enumerate(list(reservas)):
        if type(reserva) is dict and reserva.get("id_cliente") == id_cliente:
            paquete = buscar_paquete(reserva.get("id_paquete"))
            if normalizar_estado_reserva(reserva.get("estado", "")) == "activa":
                if paquete is not None:
                    paquete["cupos"] += reserva.get("personas", 0)
            if paquete is not None and ('precio_unitario' not in reserva or reserva['precio_unitario'] is None):
                reserva['precio_unitario'] = paquete.get('precio')
            reserva["estado"] = "cancelada"
            canceladas += 1
        elif type(reserva) is list and len(reserva) > 1 and reserva[1] == id_cliente:
            destino = reserva[2] if len(reserva) > 2 else ""
            personas = reserva[3] if len(reserva) > 3 else 0
            reservas[indice] = {
                "id_reserva": reserva[0],
                "id_cliente": reserva[1],
                "id_paquete": None,
                "destino": destino,
                "personas": personas,
                "estado": "cancelada",
                "precio_unitario": None,
            }
            canceladas += 1
    if canceladas:
        print(f"Reservas asociadas canceladas: {canceladas}")

    print(f"El cliente {cliente['nombre']} ahora figura con estado {formatear_estado(cliente['estado'])}.")


def buscar_paquete(id_paquete):
    for paquete in paquetes:
        if paquete["id_paquete"] == id_paquete:
            return paquete
    return None
