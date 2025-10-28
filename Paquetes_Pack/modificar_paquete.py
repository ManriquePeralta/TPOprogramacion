# Modificacion de paquetes con validaciones consistentes.

from Paquetes_Pack.mostrar_paquetes import mostrar_paquetes
from Paquetes_Pack.funciones_aux import (
    es_fecha_valida,
    es_numero_positivo,
    mostrar_error,
    comparar_fechas,
    buscar_indice_por_id,
    cargar_paquete_desde_archivo,
    guardar_paquete_en_archivo,
)
from Reservas_Pack.funciones_aux import reservas

TIPOS_VALIDOS = ("Estandar", "Premium", "Full")


def modificar_paquete():
    # Permite editar campos del paquete manteniendo datos consistentes.
    paquetes = cargar_paquete_desde_archivo()
    # Muestra el listado como referencia antes de solicitar el ID.
    mostrar_paquetes()

    id_paquete_txt = input("\nIngrese el ID del paquete a modificar (0 para salir): ").strip()
    if id_paquete_txt == "0":
        print("Operacion cancelada.")
        return

    if not id_paquete_txt.isdigit():
        mostrar_error("El ID debe ser un numero positivo.")
        return

    id_paquete = int(id_paquete_txt)
    indice = buscar_indice_por_id(paquetes, id_paquete)
    if indice == -1:
        mostrar_error("ID de paquete no encontrado.")
        return

    paquete = paquetes[indice]
    print("Deje vacio para mantener el valor actual.")

    destino = input(f"Destino ({paquete['destino']}): ").strip()
    if destino:
        # Asigna el nuevo destino cuando el usuario lo provee.
        paquete["destino"] = destino

    precio_txt = input(f"Precio ({paquete['precio']}): ").strip()
    if precio_txt:
        if not es_numero_positivo(precio_txt):
            mostrar_error("El precio debe ser un numero positivo.")
            return
        nuevo_precio = int(precio_txt)
        precio_anterior = paquete["precio"]
        if nuevo_precio != precio_anterior:
            congelar_precio_reservas(id_paquete, paquete["destino"], precio_anterior)
        paquete["precio"] = nuevo_precio

    fecha_inicio = input(f"Fecha inicio ({paquete['fecha_inicio']}): ").strip()
    fecha_fin = input(f"Fecha fin ({paquete['fecha_fin']}): ").strip()
    if fecha_inicio or fecha_fin:
        # Utiliza los valores existentes cuando se dejan campos en blanco.
        fecha_inicio = fecha_inicio or paquete["fecha_inicio"]
        fecha_fin = fecha_fin or paquete["fecha_fin"]
        if not es_fecha_valida(fecha_inicio) or not es_fecha_valida(fecha_fin):
            mostrar_error("Las fechas deben tener formato dd/mm/yyyy.")
            return
        if not comparar_fechas(fecha_inicio, fecha_fin):
            mostrar_error("La fecha de fin no puede ser anterior a la de inicio.")
            return
        paquete["fecha_inicio"] = fecha_inicio
        paquete["fecha_fin"] = fecha_fin

    cupos_txt = input(f"Cupos ({paquete['cupos']}): ").strip()
    if cupos_txt:
        if not es_numero_positivo(cupos_txt):
            mostrar_error("Los cupos deben ser un numero positivo.")
            return
        # Actualiza la capacidad disponible del paquete.
        paquete["cupos"] = int(cupos_txt)

    tipo = input(f"Tipo ({paquete['tipo']}): ").strip()
    if tipo:
        tipo = tipo.capitalize()
        if tipo not in TIPOS_VALIDOS:
            mostrar_error("Tipo invalido. Opciones: Estandar, Premium o Full.")
            return
        paquete["tipo"] = tipo

    descripcion = input(f"Descripcion ({paquete['descripcion']}): ").strip()
    if descripcion:
        # Guarda la nueva descripcion del paquete.
        paquete["descripcion"] = descripcion

    if guardar_paquete_en_archivo(paquetes):
        print(f"Paquete ID {id_paquete} actualizado correctamente.")
    else:
        mostrar_error("No se pudieron guardar los cambios del paquete.")


def congelar_precio_reservas(id_paquete, destino_paquete, precio_original):
    # Asegura que las reservas conserven el precio original del paquete.
    for indice, reserva in enumerate(reservas):
        if type(reserva) is dict:
            # Solo interviene sobre las reservas ligadas al paquete.
            mismo_paquete = reserva.get("id_paquete") == id_paquete
            precio_guardado = reserva.get("precio_unitario")
            if mismo_paquete and precio_guardado is None:
                reserva["precio_unitario"] = precio_original
        elif len(reserva) > 2:
            # Normaliza reservas almacenadas como listas para evitar inconsistencias.
            destino_actual = reserva[2]
            coincide_destino = destino_actual == destino_paquete or destino_actual == id_paquete
            if coincide_destino:
                id_reserva = reserva[0]
                id_cliente = reserva[1] if len(reserva) > 1 else None
                personas = reserva[3] if len(reserva) > 3 else 0
                estado = reserva[4] if len(reserva) > 4 else "activa"
                reservas[indice] = {
                    "id_reserva": id_reserva,
                    "id_cliente": id_cliente,
                    "id_paquete": id_paquete,
                    "destino": destino_actual,
                    "personas": personas,
                    "estado": estado,
                    "precio_unitario": precio_original,
                }
