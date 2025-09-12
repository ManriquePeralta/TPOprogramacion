import re

def es_fecha_valida(fecha):
    """Verifica si la fecha tiene formato dd/mm/yyyy y solo números."""
    return re.match(r"^\d{2}/\d{2}/\d{4}$", fecha) is not None

def es_numero_positivo(valor):
    """Verifica si el valor es un número entero positivo."""
    return valor.isdigit() and int(valor) >= 0

def mostrar_error(msg):
    print(f"❌ {msg}")
