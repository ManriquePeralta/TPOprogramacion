# Funciones auxiliares para la gestion de reservas.

from .crear_lista import leer_reservas_txt, guardar_reservas_txt
import re

try:
    reservas = leer_reservas_txt()
except Exception:
    # Si el archivo no existe o esta corrupto, se trabaja con una lista vacia
    reservas = []
# Lista global que representa las reservas cargadas en memoria.


def guardar_reservas():
    # Guarda la lista global de reservas en el archivo TXT.
    guardar_reservas_txt(reservas)

ESTADOS_VALIDOS = ("activa", "cancelada")


def normalizar_estado(estado):
    # Devuelve el estado en minusculas y sin espacios extra.
    return estado.strip().lower()


def formatear_estado(estado):
    # Formatea un estado para mostrarlo con mayuscula inicial.
    return normalizar_estado(estado).capitalize()


def validar_id(texto):
    # Valida que el texto represente un numero entero positivo.
    return bool(re.match(r"^\d+$", texto or ""))


def validar_cantidad_personas(texto):
    # Valida que represente una cantidad mayor o igual a 1.
    return bool(re.match(r"^[1-9]\d*$", texto or ""))


def generar_nuevo_id(reservas):
    # Obtiene el siguiente ID disponible a partir de la lista de reservas.
    if not reservas:
        return 1
    return max(reserva["id_reserva"] for reserva in reservas) + 1


def ordenar_reservas(reservas, clave="id_reserva"):
    # Devuelve una nueva lista de reservas ordenada por la clave indicada.
    return sorted(reservas, key=lambda reserva: reserva[clave])


def buscar_indice_por_id(reservas, id_reserva):
    # Devuelve el indice de la reserva con el ID indicado, o -1 si no existe.
    indices = {
        reservas[indice]["id_reserva"]: indice
        for indice in range(len(reservas))
    }
    return indices.get(id_reserva, -1)


def obtener_reserva_por_id(reservas, id_reserva):
    # Devuelve la reserva con el ID indicado, o None si no existe.
    indice = buscar_indice_por_id(reservas, id_reserva)
    return reservas[indice] if indice != -1 else None


def reservas_por_estado(reservas, estado_buscado):
    # Filtra las reservas por estado (case insensitive).
    estado_buscado = normalizar_estado(estado_buscado)
    return [reserva for reserva in reservas if normalizar_estado(reserva["estado"]) == estado_buscado]


def contar_por_estado(reservas):
    # Cuenta cuantas reservas hay por estado.
    conteo = {}
    for reserva in reservas:
        estado = normalizar_estado(reserva["estado"])
        conteo[estado] = conteo.get(estado, 0) + 1
    return conteo


def reservas_por_cliente(reservas, id_cliente, solo_activas=False):
    # Obtiene las reservas de un cliente, opcionalmente solo activas.
    resultado = []
    for reserva in reservas:
        if reserva["id_cliente"] == id_cliente:
            if solo_activas and normalizar_estado(reserva["estado"]) != "activa":
                continue
            resultado.append(reserva)
    return resultado


def reservas_por_paquete(reservas, id_paquete, solo_activas=False):
    # Devuelve reservas asociadas a un paquete determinado.
    seleccionadas = []
    for reserva in reservas:
        if reserva["id_paquete"] == id_paquete:
            if solo_activas and normalizar_estado(reserva["estado"]) != "activa":
                continue
            seleccionadas.append(reserva)
    return seleccionadas

