"""Cancelacion de reservas con restauracion de cupos."""

from Reservas_Pack.lista_reservas import reservas
from Reservas_Pack.funciones_aux import validar_id, obtener_reserva_por_id, formatear_estado
from Reservas_Pack.mostrar_reservas import mostrar_reservas
from Paquetes_Pack.lista_paquetes import paquetes


def eliminar_reserva():
    print("\n\n=== CANCELAR RESERVA ===")
    mostrar_reservas(interactivo=False)

    id_reserva_txt = input("\nIngrese el ID de la reserva a cancelar (0 para salir): ").strip()
    if id_reserva_txt == "0":
        print("Operacion cancelada.")
        return

    while not validar_id(id_reserva_txt):
        print("ID invalido. Debe ser un numero positivo.")
        id_reserva_txt = input("Ingrese el ID de la reserva a cancelar (0 para salir): ").strip()
        if id_reserva_txt == "0":
            print("Operacion cancelada.")
            return

    id_reserva = int(id_reserva_txt)
    reserva = obtener_reserva_por_id(reservas, id_reserva)
    if reserva is None:
        print("No se encontro una reserva con ese ID.")
        return

    if reserva["estado"].lower() == "cancelada":
        print("La reserva ya se encuentra cancelada.")
        return

    confirmar = input("Confirma cancelar la reserva? (s/n): ").strip().lower()
    while confirmar not in ("s", "n"):
        confirmar = input("Respuesta invalida. Confirma cancelar la reserva? (s/n): ").strip().lower()

    if confirmar == "n":
        print("Operacion cancelada por el usuario.")
        return

    paquete = buscar_paquete(reserva["id_paquete"])
    if paquete is not None:
        paquete["cupos"] += reserva["personas"]

    reserva["estado"] = "cancelada"
    print(f"Reserva ID {id_reserva} marcada como {formatear_estado(reserva['estado'])}.")


def buscar_paquete(id_paquete):
    for paquete in paquetes:
        if paquete["id_paquete"] == id_paquete:
            return paquete
    return None
