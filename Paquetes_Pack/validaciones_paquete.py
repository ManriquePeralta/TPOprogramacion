"""
Módulo de funciones auxiliares para validaciones de datos de paquetes turísticos.
Incluye validación de fechas, números y mensajes de error.
"""

import re
from datetime import datetime


def comparar_fechas(fecha_inicio: str, fecha_fin: str) -> bool:

    formato = "%d/%m/%Y"  # dd/mm/yyyy

    inicio = datetime.strptime(fecha_inicio, formato)
    fin = datetime.strptime(fecha_fin, formato)

    return inicio <= fin
    """
    Compara dos fechas en formato dd/mm/yyyy.
    Devuelve True si la fecha de inicio es anterior o igual a la de fin.
    """

def es_fecha_valida(fecha):
    return re.match(r"^\d{2}/\d{2}/\d{4}$", fecha) is not None
    """
    Verifica si la fecha tiene formato dd/mm/yyyy y solo números.
    """

def es_numero_positivo(valor):
    """Verifica si el valor es un número entero positivo."""
    return valor.isdigit() and int(valor) >= 0

def mostrar_error(msg):
    print(f"❌ {msg}")

