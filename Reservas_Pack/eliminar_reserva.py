# Cancelacion de reservas con restauracion de cupos.

from Reservas_Pack.funciones_aux import (
    reservas,
    guardar_reservas,
    validar_id,
    obtener_reserva_por_id,
    formatear_estado,
)
from Reservas_Pack.mostrar_reservas import mostrar_reservas
from Paquetes_Pack.funciones_aux import cargar_paquete_desde_archivo, guardar_paquete_en_archivo


def eliminar_reserva():
    # Cancela una reserva, libera cupos y persiste los cambios.
    print("\n\n=== CANCELAR RESERVA ===")
    mostrar_reservas(interactivo=False)

    # Solicita el identificador y permite cancelar la operacion.
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

    # Restaura cupos del paquete asociado antes de actualizar el estado.
    paquetes = cargar_paquete_desde_archivo()
    paquete = buscar_paquete(paquetes, reserva["id_paquete"])
    if paquete:
        paquete["cupos"] += reserva["personas"]

    reserva["estado"] = "cancelada"
    
    # Guardar cambios en TXT
    guardar_reservas()


    print(f"Reserva ID {id_reserva} marcada como {formatear_estado(reserva['estado'])}.")

    if not guardar_paquete_en_archivo(paquetes):
        print("Advertencia: no se pudieron guardar los cambios de cupos.")


def buscar_paquete(paquetes, id_paquete):
    # Devuelve el paquete con el ID solicitado, si existe.
    for paquete in paquetes:
        if paquete["id_paquete"] == id_paquete:
            return paquete
    return None
