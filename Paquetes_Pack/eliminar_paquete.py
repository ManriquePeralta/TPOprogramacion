# Baja de paquetes (eliminacion definitiva).

from Paquetes_Pack.mostrar_paquetes import mostrar_paquetes
from Paquetes_Pack.funciones_aux import (
    mostrar_error,
    buscar_indice_por_id,
    cargar_paquete_desde_archivo,
    guardar_paquete_en_archivo,
)
from Reservas_Pack.funciones_aux import reservas


def eliminar_paquete():
    # Elimina un paquete y cancela las reservas asociadas.
    paquetes = cargar_paquete_desde_archivo()
    listado = mostrar_paquetes()
    if not listado:
        return

    # Solicita el identificador y ofrece una salida rapida.
    id_paquete_txt = input("\nIngrese el ID del paquete a eliminar (0 para salir): ").strip()
    if id_paquete_txt == "0":
        print("Operacion cancelada.")
        return

    if not id_paquete_txt.isdigit():
        mostrar_error("El ID debe ser un numero positivo.")
        return

    id_paquete = int(id_paquete_txt)
    indice = buscar_indice_por_id(paquetes, id_paquete)
    if indice == -1:
        mostrar_error("No se encontro un paquete con ese ID.")
        return

    paquete = paquetes[indice]
    destino_paquete = paquete["destino"]

    # Confirma la eliminacion definitiva con el usuario.
    confirmar = input(f"Confirma eliminar el paquete hacia {destino_paquete}? (s/n): ").strip().lower()
    while confirmar not in ("s", "n"):
        confirmar = input("Respuesta invalida. Confirma eliminar el paquete? (s/n): ").strip().lower()

    if confirmar == "n":
        print("Operacion cancelada por el usuario.")
        return

    canceladas = cancelar_reservas(id_paquete, destino_paquete, paquete["precio"])
    paquetes.pop(indice)
    if guardar_paquete_en_archivo(paquetes):
        print(f"Paquete ID {id_paquete} eliminado con exito.")
        if canceladas:
            print(f"Reservas canceladas automaticamente: {canceladas}.")
    else:
        mostrar_error("No se pudo guardar la lista de paquetes actualizada.")


def cancelar_reservas(id_paquete, destino_paquete, precio_paquete):
    # Marca como canceladas las reservas vinculadas al paquete eliminado.
    canceladas = 0
    # Recorre todas las reservas para localizar las asociadas.
    for posicion, reserva in enumerate(reservas):
        if type(reserva) is dict and reserva.get("id_paquete") == id_paquete:
            # Mantiene la trazabilidad del precio y destino originales.
            if reserva.get("estado", "").lower() != "cancelada":
                canceladas += 1
            if reserva.get("precio_unitario") is None:
                reserva["precio_unitario"] = precio_paquete
            if reserva.get("destino") is None:
                reserva["destino"] = destino_paquete
            reserva["estado"] = "cancelada"
        elif type(reserva) is list and len(reserva) >= 4 and reserva[2] == destino_paquete:
            # Normaliza reservas en formato lista al convertirlas en diccionarios.
            reservas[posicion] = {
                "id_reserva": reserva[0],
                "id_cliente": reserva[1],
                "id_paquete": id_paquete,
                "destino": destino_paquete,
                "personas": reserva[3],
                "estado": "cancelada",
                "precio_unitario": precio_paquete,
            }
            canceladas += 1
    return canceladas
