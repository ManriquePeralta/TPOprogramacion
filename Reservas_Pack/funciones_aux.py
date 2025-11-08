# Funciones auxiliares para la gestion de reservas.

from .crear_lista import leer_reservas_txt, guardar_reservas_txt
import re

reservas = leer_reservas_txt()
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


def busqueda_secuencial(lista, clave, valor, retornar_indice=False):
    # Busca el primer elemento cuyo campo coincide con el valor indicado.
    for indice, elemento in enumerate(lista):
        if elemento.get(clave) == valor:
            return indice if retornar_indice else elemento
    return -1 if retornar_indice else None

def busqueda_secuencial_reservas(reservas,clave,valor):
    # Busca en la lista de reservas el primer elemento cuyo campoo coincide con el valor indicado 
    for inidice,reserva in enumerate(reservas):
        
        print(reserva[clave])
        if str(reserva[clave])==valor:
            return reserva 
    
    return -1


def obtener_paquete_disponible(paquetes, id_paquete):
    # Devuelve el paquete con cupos disponibles o un mensaje de error.
    paquete = busqueda_secuencial(paquetes, "id_paquete", id_paquete)
    if paquete is None:
        return None, "No existe un paquete con ese ID."
    if paquete.get("cupos", 0) <= 0:
        return None, "El paquete no tiene cupos disponibles."
    return paquete, None


def validar_cupos_disponibles(paquete, cantidad):
    # Confirma que la cantidad solicitada no exceda los cupos.
    return cantidad <= paquete.get("cupos", 0)




def obtener_reserva_activa(reservas_lista, id_reserva):
    # Devuelve la reserva si existe y no esta cancelada.
    
    reserva = busqueda_secuencial_reservas(reservas_lista, 0, id_reserva)
    if reserva is -1:
        return None, "No se encontro una reserva con ese ID."
    if normalizar_estado(reserva[5]) == "cancelada":
        return None, "La reserva ya se encuentra cancelada."
    return reserva, None


def restaurar_cupos(paquetes, id_paquete, cantidad):
    # Busca el paquete y le restaura los cupos cancelados.
    paquete = busqueda_secuencial(paquetes, "id_paquete", id_paquete)
    # Si se encontro el paquete, restaura los cupos 
    if paquete is not None:
        paquete["cupos"] = paquete.get("cupos", 0) + cantidad
    return paquete


def generar_nuevo_id(reservas):
    # Obtiene el siguiente ID disponible a partir de la lista de reservas.
    if not reservas:
        return 1
    return max(reserva[0] for reserva in reservas) + 1


def ordenar_reservas(reservas):
    # Devuelve una nueva lista de reservas ordenada por la clave indicada.
    return sorted(reservas, key=lambda reserva: reserva[0])


def reservas_por_estado(reservas, estado_buscado):
    # Filtra las reservas por estado (case insensitive).
    estado_buscado = normalizar_estado(estado_buscado)
    # Retorna la lista de resrevas que coinciden con el estado buscado 
    return [reserva for reserva in reservas if normalizar_estado(reserva["estado"]) == estado_buscado]


def contar_por_estado(reservas):
    # Cuenta cuantas reservas hay por estado.
    conteo = {}
    # Recorre todas las reservas y actualiza el conteo por estado 
    for reserva in reservas:
        estado = normalizar_estado(reserva[5])
        conteo[estado] = conteo.get(estado, 0) + 1
    return conteo


def reservas_por_cliente(reservas, id_cliente, solo_activas=False):
    # Obtiene las reservas de un cliente, opcionalmente solo activas.
    resultado = []
    for reserva in reservas:
        # Verifica si la reserva pertenece al cliente indicado 
        if reserva[1] == id_cliente:
            # Verifica que se filtren solo las reservas activas 
            if solo_activas and normalizar_estado(reserva[5]) != "activa":
                continue
            resultado.append(reserva)
    return resultado


def reservas_por_paquete(reservas, id_paquete, solo_activas=False):
    # Devuelve reservas asociadas a un paquete determinado.
    seleccionadas = []
    for reserva in reservas:
        if reserva[2] == id_paquete:
            if solo_activas and normalizar_estado(reserva[5]) != "activa":
                continue
            seleccionadas.append(reserva)
    return seleccionadas
