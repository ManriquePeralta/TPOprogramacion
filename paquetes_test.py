from Paquetes_Pack.funciones_aux import es_numero_positivo, comparar_fechas, es_fecha_valida
from Paquetes_Pack.lista_paquetes import paquetes

def test_es_numero_positivo():
    assert es_numero_positivo("10") == True
    assert es_numero_positivo("-5") == False
    assert es_numero_positivo("abc") == False
    assert es_numero_positivo("=") == False

def test_comparar_fechas():
    assert comparar_fechas("01/01/2024", "02/01/2024") == True
    assert comparar_fechas("10/01/2024", "05/01/2024") == False


def test_modificar_paquete():
    assert es_numero_positivo("1000") == True, "bien"
    assert es_numero_positivo("-50") == False, "num negativ no"
    assert es_numero_positivo("abc") == False, "palabras no, numeros"
    assert es_numero_positivo("5000000000") == True, "joya"
   

    assert es_fecha_valida("10/10/2025") == True, "perf"
    assert es_fecha_valida("99/02/2024") == False, "feb no 31 ni 30 ni siempre 29"
    assert es_fecha_valida("10-10-2025") == False, "mal el formato"  
    assert es_fecha_valida("12-2-2025") == False, "mal el formato"
    assert es_fecha_valida("2025/12/01") == False, "Orden incorrecto de día, mes y año"


