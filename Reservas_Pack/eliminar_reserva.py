# Cancelacion de reservas con restauracion de cupos.

from Reservas_Pack.funciones_aux import (
    reservas,
    guardar_reservas,
    validar_id,
    formatear_estado,
    obtener_reserva_activa,
    restaurar_cupos,
)
from Reservas_Pack.mostrar_reservas import mostrar_reservas
from Paquetes_Pack.funciones_aux import cargar_paquete_desde_archivo, guardar_paquete_en_archivo


def eliminar_reserva():
    # Cancela una reserva, libera cupos y persiste los cambios.
    print("\n\n=== CANCELAR RESERVA ===")
    mostrar_reservas(interactivo=False)

    if not reservas:
        print("No hay reservas cargadas para cancelar.")
        return

    reserva_seleccionada = None
    id_reserva = None
    # Seleccionar reserva a cancelar
    while reserva_seleccionada is None:
        id_reserva_txt = input("\nIngrese el ID de la reserva a cancelar (0 para salir): ").strip()
        if id_reserva_txt == "0":
            print("Operacion cancelada.")
            return
        # Validar ID de la reserva
        if not validar_id(id_reserva_txt):
            print("ID invalido. Debe ser un numero positivo.")
        else:
            # Buscar reserva activa por ID 
            id_reserva = id_reserva_txt
            reserva, error = obtener_reserva_activa(reservas, id_reserva)
            if error:
                print(error)
            else:
                reserva_seleccionada = reserva
    # Confirmar cancelacion de la reserva
    confirmar = input("Confirma cancelar la reserva? (s/n): ").strip().lower()
    while confirmar not in ("s", "n"):
        confirmar = input("Respuesta invalida. Confirma cancelar la reserva? (s/n): ").strip().lower()

    if confirmar == "n":
        print("Operacion cancelada por el usuario.")
        return

    # Restaura cupos del paquete asociado antes de actualizar el estado.
    paquetes = cargar_paquete_desde_archivo()
    restaurar_cupos(paquetes, reserva_seleccionada[2], reserva_seleccionada[4])

    reserva_seleccionada[5] = "cancelada"
    
    # Guardar cambios en TXT
    guardar_reservas()


    print(f"Reserva ID {id_reserva} marcada como {formatear_estado(reserva_seleccionada[5])}.")

    guardar_paquete_en_archivo(paquetes)
