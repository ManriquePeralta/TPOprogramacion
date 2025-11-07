# Modificacion de reservas con control de cupos y estado.

from Reservas_Pack.funciones_aux import (
    reservas,
    guardar_reservas,
    validar_id,
    validar_cantidad_personas,
    normalizar_estado,
    formatear_estado,
    ESTADOS_VALIDOS,
    busqueda_secuencial_reservas,
    busqueda_secuencial
)
from Reservas_Pack.mostrar_reservas import mostrar_reservas
from Paquetes_Pack.funciones_aux import (
    cargar_paquete_desde_archivo,
    guardar_paquete_en_archivo,
)
from Paquetes_Pack.mostrar_paquetes import mostrar_paquetes


def modificar_reserva():
    # Presenta opciones para modificar cantidad, paquete o estado.
    mostrar_reservas(interactivo=False)
    # Solicita el identificador y da la chance de cancelar la edicion.
    id_reserva = input("\nIngrese el ID de la reserva a modificar (0 para salir): ").strip()
    if id_reserva == "0":
        print("Operacion cancelada.")
        return

    while not validar_id(id_reserva):
        print("ID invalido. Debe ser un numero positivo.")
        id_reserva = input("Ingrese el ID de la reserva a modificar (0 para salir): ").strip()
        if id_reserva == "0":
            print("Operacion cancelada.")
            return

    id_reserva = int(id_reserva)
    reserva = busqueda_secuencial_reservas(reservas, 0, id_reserva)
    if reserva is None:
        print("No se encontro una reserva con ese ID.")
        return

    # Obtiene la informacion de paquetes para reutilizarla en varias opciones.
    paquetes = cargar_paquete_desde_archivo()

    opcion = ""
    while opcion != "0":
        print("\n=== MODIFICAR RESERVA ===")
        print("1. Cambiar cantidad de personas")
        print("2. Cambiar paquete")
        print("3. Cambiar estado")
        print("0. Volver")
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            # Ajusta la cantidad de pasajeros reservados.
            modificar_cantidad(reserva, paquetes)
        elif opcion == "2":
            # Permite cambiar el paquete asociado.
            modificar_paquete(reserva, paquetes)
        elif opcion == "3":
            # Actualiza el estado (activa/cancelada).
            modificar_estado(reserva, paquetes)
        elif opcion == "0":
            print("Regresando al menu de reservas...")
        else:
            print("Opcion invalida. Intente nuevamente.")
      
        # Guardar cambios cada vez que se modifica algo
        guardar_reservas()


def modificar_cantidad(reserva, paquetes):
    # Ajusta la cantidad de personas respetando los cupos disponibles.
    paquete = busqueda_secuencial(paquetes, "id_paquete",reserva[2])
    if paquete is None:
        print("No se encontro el paquete asociado a la reserva.")
        return

    disponible = paquete["cupos"] + reserva[4] if normalizar_estado(reserva[5]) == "activa" else paquete["cupos"]
    if disponible == 0:
        print("No hay cupos disponibles para ajustar la cantidad.")
        return

    print(f"Cupos disponibles para el paquete: {disponible}")
    cantidad_personas = input("Nueva cantidad de personas: ").strip()
    while not validar_cantidad_personas(cantidad_personas):
        print("La cantidad debe ser un numero entero mayor a 0.")
        cantidad_personas = input("Nueva cantidad de personas: ").strip()
    nueva_cantidad = int(cantidad_personas)

    if normalizar_estado(reserva[5]) == "activa":
        if nueva_cantidad > disponible:
            print("No es posible aumentar tanto la reserva. Cupos insuficientes.")
            return
        # Ajusta los cupos restando solo la diferencia con el valor previo.
        paquete["cupos"] = paquete["cupos"] + reserva[4] - nueva_cantidad
    else:
        if nueva_cantidad > paquete["cupos"]:
            print("No es posible asignar esa cantidad porque el paquete no tiene cupos.")
            return
        # Reactiva la reserva y descuenta cupos del paquete seleccionado.
        paquete["cupos"] -= nueva_cantidad
        reserva[5] = "activa"
        print("La reserva se reactivo automaticamente al asignar cupos.")

    reserva[4] = nueva_cantidad
    print("Cantidad de personas actualizada correctamente.")
    
    guardar_paquete_en_archivo(paquetes)


def modificar_paquete(reserva, paquetes):
    # Permite reasignar la reserva a otro paquete compatible.
    paquete_actual = busqueda_secuencial(paquetes, "id_paquete", reserva[2])
    personas = reserva[4]

    mostrar_paquetes()
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
    paquete_nuevo = busqueda_secuencial(paquetes, "id_paquete", id_paquete_nuevo)

    if paquete_nuevo is None:
        print("No existe un paquete con ese ID.")
        return
    if paquete_nuevo["id_paquete"] == reserva[2]:
        print("La reserva ya esta asociada a ese paquete.")
        return

    disponible_nuevo = paquete_nuevo["cupos"]
    if normalizar_estado(reserva[5]) == "activa":
        if personas > disponible_nuevo:
            print("El paquete seleccionado no tiene cupos suficientes.")
            return
        paquete_nuevo["cupos"] -= personas
        if paquete_actual is not None:
            # Devuelve los cupos al paquete original si la reserva se traslada.
            paquete_actual["cupos"] += personas
    else:
        if personas > disponible_nuevo:
            print("El paquete no tiene cupos suficientes para reactivar la reserva.")
            return
        paquete_nuevo["cupos"] -= personas
        if paquete_actual is not None:
            if normalizar_estado(reserva[3]) == "activa":
                paquete_actual["cupos"] += personas
        # Reactiva la reserva al asignarla a un paquete con disponibilidad.
        reserva[5] = "activa"
        print("La reserva se reactivo con el nuevo paquete.")

    reserva[2] = id_paquete_nuevo
    # Actualiza la tarifa de referencia con el precio del nuevo paquete.
    reserva[6] = paquete_nuevo.get("precio")
    print("Paquete actualizado correctamente.")
    guardar_paquete_en_archivo(paquetes)


def modificar_estado(reserva, paquetes):
    # Cambia el estado entre activo y cancelado actualizando cupos.
    estado_actual = normalizar_estado(reserva[5])
    print(f"Estado actual: {formatear_estado(estado_actual)}")
    print("Estados disponibles: Activa / Cancelada")
    nuevo_estado = input("Ingrese el nuevo estado: ").strip().lower()
    while nuevo_estado not in ESTADOS_VALIDOS:
        print("Estado invalido. Opciones validas: Activa o Cancelada.")
        nuevo_estado = input("Ingrese el nuevo estado: ").strip().lower()

    if nuevo_estado == estado_actual:
        print("La reserva ya posee ese estado.")
        return

    paquete = busqueda_secuencial(paquetes, "id_paquete", reserva[2])
    personas = reserva[4]

    if estado_actual == "activa" and nuevo_estado != "activa":
        if paquete is not None:
            # Al cancelar se liberan los cupos previamente asignados.
            paquete["cupos"] += personas
    elif estado_actual != "activa" and nuevo_estado == "activa":
        if paquete is None or personas > paquete["cupos"]:
            print("No hay cupos suficientes para reactivar la reserva.")
            return
        # Al reactivar se consumen cupos de la disponibilidad actual.
        paquete["cupos"] -= personas

    reserva[5] = nuevo_estado
    print(f"Estado actualizado: {formatear_estado(reserva[5])}.")
    guardar_paquete_en_archivo(paquetes)
