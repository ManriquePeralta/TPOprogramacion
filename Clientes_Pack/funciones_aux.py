"""Funciones auxiliares y validaciones para el modulo de clientes."""

import re


def normalizar_estado(estado):
    """Devuelve el estado en minusculas sin espacios extra."""
    return estado.strip().lower()


def formatear_estado(estado):
    """Convierte un estado a formato de presentacion (capitalizado)."""
    return normalizar_estado(estado).capitalize()


def ordenar_clientes(clientes, clave="id"):
    """Ordena una copia de la lista de clientes segun la clave indicada."""
    return sorted(clientes, key=lambda cliente: cliente.get(clave))


def buscar_indice_por_id(clientes, id_cliente):
    """Busca el indice del cliente por ID. Devuelve -1 si no existe."""
    indices = {
        clientes[indice].get("id"): indice
        for indice in range(len(clientes))
    }
    return indices.get(id_cliente, -1)


def buscar_indice_por_dni(clientes, dni):
    """Busca el indice del cliente por DNI. Devuelve -1 si no existe."""
    indices = {
        clientes[indice].get("dni"): indice
        for indice in range(len(clientes))
    }
    return indices.get(dni, -1)


def validar_id(texto):
    """Valida que el texto represente un ID numerico positivo."""
    return bool(re.match(r"^\d+$", texto or ""))


def validar_dni(texto):
    """Valida que el DNI tenga exactamente 8 digitos."""
    return bool(re.match(r"^\d{8}$", texto or ""))


def validar_nombre(nombre):
    """Valida que el nombre tenga letras y espacios, con longitud minima."""
    if len(nombre.strip()) < 3:
        return False
    patron = r"^[A-Za-z\u00C1\u00C9\u00CD\u00D3\u00DA\u00E1\u00E9\u00ED\u00F3\u00FA\u00F1\u00D1 ]+$"
    return bool(re.match(patron, nombre.strip()))


def validar_email(email):
    """Valida un email basico usando una expresion simple."""
    patron = r"^[\w\.-]+@[\w\.-]+\.[A-Za-z]{2,}$"
    return bool(re.match(patron, email.strip()))


def contar_por_estado(clientes):
    """Cuenta cuantos clientes hay por cada estado."""
    conteo = {}
    for cliente in clientes:
        estado = normalizar_estado(cliente.get("estado", ""))
        conteo[estado] = conteo.get(estado, 0) + 1
    return conteo


def clientes_por_estado(clientes, estado_buscado):
    """Filtra clientes por estado normalizado."""
    estado_buscado = normalizar_estado(estado_buscado)
    return [cliente for cliente in clientes if normalizar_estado(cliente.get("estado", "")) == estado_buscado]


def obtener_reservas_de_cliente(reservas, id_cliente):
    """Devuelve las reservas asociadas a un cliente dado su ID."""
    coincidencias = []
    for reserva in reservas:
        if type(reserva) is dict:
            if reserva.get("id_cliente") == id_cliente:
                coincidencias.append(reserva)
        elif len(reserva) > 1 and reserva[1] == id_cliente:
            coincidencias.append(reserva)
    return coincidencias


def resumen_estados(clientes):
    """Devuelve (total, activos, inactivos, otros)."""
    total = len(clientes)
    conteo = contar_por_estado(clientes)
    activos = conteo.get("activo", 0)
    inactivos = conteo.get("inactivo", 0)
    otros = total - activos - inactivos
    return total, activos, inactivos, otros
