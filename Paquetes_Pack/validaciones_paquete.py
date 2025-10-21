"""
Módulo de funciones auxiliares para validaciones de datos de paquetes turísticos.
Incluye validación de fechas, números y mensajes de error.
"""

import re
from datetime import datetime


def comparar_fechas(fecha_inicio: str, fecha_fin: str) -> bool:
    """
    Compara dos fechas en formato dd/mm/yyyy.
    Devuelve True si la fecha de inicio es anterior o igual a la de fin.
    Si alguna fecha no es valida (por ejemplo 31/02/2024) devuelve False.
    """
    formato = "%d/%m/%Y"  
    try:
        inicio = datetime.strptime(fecha_inicio, formato)
        fin = datetime.strptime(fecha_fin, formato)
    except ValueError:
        return False

    return inicio <= fin

def es_fecha_valida(fecha: str) -> bool:
    """
    Verifica que la cadena tenga formato dd/mm/yyyy y represente
    una fecha real (por ejemplo no acepta 34/06/2020, 12/14/2020 o 31/02/2024).
    """
    if re.match(r"^\d{2}/\d{2}/\d{4}$", fecha) is None:
        return False

    formato = "%d/%m/%Y"
    try:
        datetime.strptime(fecha, formato)
        return True
    except ValueError:
        return False

def es_numero_positivo(valor):
    """Verifica si el valor es un número entero positivo."""
    return valor.isdigit() and int(valor) >= 0

def mostrar_error(msg):
    print(f"ERROR. {msg}")

