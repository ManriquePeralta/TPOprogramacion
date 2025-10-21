"""Baja de paquetes (eliminacion definitiva)."""

from Paquetes_Pack.lista_paquetes import paquetes
from Paquetes_Pack.mostrar_paquetes import listar_paquetes
from Paquetes_Pack.funciones_aux import mostrar_error, buscar_indice_por_id
from Reservas_Pack.lista_reservas import reservas


def eliminar_paquete():
    listar_paquetes()

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
    destino_paquete = paquete['destino']

    confirmar = input(f"Confirma eliminar el paquete hacia {destino_paquete}? (s/n): ").strip().lower()
    while confirmar not in ("s", "n"):
        confirmar = input("Respuesta invalida. Confirma eliminar el paquete? (s/n): ").strip().lower()

    if confirmar == "n":
        print("Operacion cancelada por el usuario.")
        return

    canceladas = 0
    precio_paquete = paquete['precio']
    reservas_copia = list(reservas)
    for idx in range(len(reservas_copia)):
        reserva = reservas_copia[idx]
        if type(reserva) is dict and reserva.get("id_paquete") == id_paquete:
            if reserva.get("estado", "").lower() != "cancelada":
                canceladas += 1
            if 'precio_unitario' not in reserva or reserva['precio_unitario'] is None:
                reserva['precio_unitario'] = precio_paquete
            reserva["estado"] = "cancelada"
            reserva.setdefault("destino", destino_paquete)
        elif type(reserva) is list and len(reserva) >= 4 and reserva[2] == destino_paquete:
            reservas[idx] = {
                "id_reserva": reserva[0],
                "id_cliente": reserva[1],
                "id_paquete": id_paquete,
                "destino": destino_paquete,
                "personas": reserva[3],
                "estado": "cancelada",
                "precio_unitario": precio_paquete,
            }
            canceladas += 1

    paquetes.pop(indice)
    print(f"Paquete ID {id_paquete} eliminado con exito.")
    if canceladas:
        print(f"Reservas canceladas automaticamente: {canceladas}.")
