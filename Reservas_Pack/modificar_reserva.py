"""Modificacion de reservas con control de cupos y estado."""

from Reservas_Pack.lista_reservas import reservas
from Reservas_Pack.funciones_aux import (
    validar_id,
    validar_cantidad_personas,
    obtener_reserva_por_id,
    normalizar_estado,
    formatear_estado,
    ESTADOS_VALIDOS,
)
from Reservas_Pack.mostrar_reservas import mostrar_reservas
from Paquetes_Pack.lista_paquetes import paquetes
from Paquetes_Pack.mostrar_paquetes import listar_paquetes


def modificar_reserva():
    mostrar_reservas(interactivo=False)
    id_reserva_txt = input("\nIngrese el ID de la reserva a modificar (0 para salir): ").strip()
    if id_reserva_txt == "0":
        print("Operacion cancelada.")
        return

    while not validar_id(id_reserva_txt):
        print("ID invalido. Debe ser un numero positivo.")
        id_reserva_txt = input("Ingrese el ID de la reserva a modificar (0 para salir): ").strip()
        if id_reserva_txt == "0":
            print("Operacion cancelada.")
            return

    id_reserva = int(id_reserva_txt)
    reserva = obtener_reserva_por_id(reservas, id_reserva)
    if reserva is None:
        print("No se encontro una reserva con ese ID.")
        return

    opcion = ""
    while opcion != "0":
        print("\n=== MODIFICAR RESERVA ===")
        print("1. Cambiar cantidad de personas")
        print("2. Cambiar paquete")
        print("3. Cambiar estado")
        print("0. Volver")
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            modificar_cantidad(reserva)
        elif opcion == "2":
            modificar_paquete(reserva)
        elif opcion == "3":
            modificar_estado(reserva)
        elif opcion == "0":
            print("Regresando al menu de reservas...")
        else:
            print("Opcion invalida. Intente nuevamente.")


def modificar_cantidad(reserva):
    paquete = buscar_paquete(reserva["id_paquete"])
    if paquete is None:
        print("No se encontro el paquete asociado a la reserva.")
        return

    disponible = paquete["cupos"] + reserva["personas"] if normalizar_estado(reserva["estado"]) == "activa" else paquete["cupos"]
    if disponible == 0:
        print("No hay cupos disponibles para ajustar la cantidad.")
        return

    print(f"Cupos disponibles para el paquete: {disponible}")
    cantidad_txt = input("Nueva cantidad de personas: ").strip()
    while not validar_cantidad_personas(cantidad_txt):
        print("La cantidad debe ser un numero entero mayor a 0.")
        cantidad_txt = input("Nueva cantidad de personas: ").strip()
    nueva_cantidad = int(cantidad_txt)

    if normalizar_estado(reserva["estado"]) == "activa":
        if nueva_cantidad > disponible:
            print("No es posible aumentar tanto la reserva. Cupos insuficientes.")
            return
        paquete["cupos"] = paquete["cupos"] + reserva["personas"] - nueva_cantidad
    else:
        if nueva_cantidad > paquete["cupos"]:
            print("No es posible asignar esa cantidad porque el paquete no tiene cupos.")
            return
        paquete["cupos"] -= nueva_cantidad
        reserva["estado"] = "activa"
        print("La reserva se reactivo automaticamente al asignar cupos.")

    reserva["personas"] = nueva_cantidad
    print("Cantidad de personas actualizada correctamente.")


def modificar_paquete(reserva):
    paquete_actual = buscar_paquete(reserva["id_paquete"])
    personas = reserva["personas"]

    listar_paquetes()
    id_paquete_txt = input("\nIngrese el ID del nuevo paquete (0 para cancelar): ").strip()
    if id_paquete_txt == "0":
        print("Operacion cancelada.")
        return
    while not validar_id(id_paquete_txt):
        print("ID invalido. Debe ser un numero positivo.")
        id_paquete_txt = input("Ingrese el ID del nuevo paquete (0 para cancelar): ").strip()
        if id_paquete_txt == "0":
            print("Operacion cancelada.")
            return
    id_paquete_nuevo = int(id_paquete_txt)
    paquete_nuevo = buscar_paquete(id_paquete_nuevo)

    if paquete_nuevo is None:
        print("No existe un paquete con ese ID.")
        return
    if paquete_nuevo["id_paquete"] == reserva["id_paquete"]:
        print("La reserva ya esta asociada a ese paquete.")
        return

    disponible_nuevo = paquete_nuevo["cupos"]
    if normalizar_estado(reserva["estado"]) == "activa":
        if personas > disponible_nuevo:
            print("El paquete seleccionado no tiene cupos suficientes.")
            return
        paquete_nuevo["cupos"] -= personas
        if paquete_actual is not None:
            paquete_actual["cupos"] += personas
    else:
        if personas > disponible_nuevo:
            print("El paquete no tiene cupos suficientes para reactivar la reserva.")
            return
        paquete_nuevo["cupos"] -= personas
        if paquete_actual is not None and normalizar_estado(reserva["estado"]) == "activa":
            paquete_actual["cupos"] += personas
        reserva["estado"] = "activa"
        print("La reserva se reactivo con el nuevo paquete.")

    reserva["id_paquete"] = id_paquete_nuevo
    reserva["precio_unitario"] = paquete_nuevo.get("precio")
    print("Paquete actualizado correctamente.")


def modificar_estado(reserva):
    estado_actual = normalizar_estado(reserva["estado"])
    print(f"Estado actual: {formatear_estado(estado_actual)}")
    print("Estados disponibles: Activa / Cancelada")
    nuevo_estado = input("Ingrese el nuevo estado: ").strip().lower()
    while nuevo_estado not in ESTADOS_VALIDOS:
        print("Estado invalido. Opciones validas: Activa o Cancelada.")
        nuevo_estado = input("Ingrese el nuevo estado: ").strip().lower()

    if nuevo_estado == estado_actual:
        print("La reserva ya posee ese estado.")
        return

    paquete = buscar_paquete(reserva["id_paquete"])
    personas = reserva["personas"]

    if estado_actual == "activa" and nuevo_estado != "activa":
        if paquete is not None:
            paquete["cupos"] += personas
    elif estado_actual != "activa" and nuevo_estado == "activa":
        if paquete is None or personas > paquete["cupos"]:
            print("No hay cupos suficientes para reactivar la reserva.")
            return
        paquete["cupos"] -= personas

    reserva["estado"] = nuevo_estado
    print(f"Estado actualizado: {formatear_estado(reserva['estado'])}.")


def buscar_paquete(id_paquete):
    for paquete in paquetes:
        if paquete["id_paquete"] == id_paquete:
            return paquete
    return None
