# importar las funciones a probar desde el módulo correspondiente
from Paquetes_Pack.funciones_aux import es_numero_positivo, comparar_fechas, es_fecha_valida

# Prueba de éxito 1: detecta valores positivos y numéricos.
def test_es_numero_positivo_valido():
    assert es_numero_positivo("10")
    assert es_numero_positivo("5000000000")

# Prueba de éxito 2: compara fechas en formato dd/mm/yyyy.
def test_comparar_fechas_en_orden():
    assert comparar_fechas("01/01/2024", "02/01/2024")
    assert comparar_fechas("10/01/2024", "10/01/2024")

 # Prueba de éxito 3: valida formato dd/mm/yyyy.
def test_es_fecha_valida_correcta():
    assert es_fecha_valida("10/10/2025")

 # Prueba de fallo 1: detecta valores no positivos o no numéricos.
def test_es_numero_positivo_falla_en_valores_invalidos():
    assert not es_numero_positivo("-5")
    assert not es_numero_positivo("abc")
    assert not es_numero_positivo("=")

 # Prueba de fallo 2: formato inválido impide la comparación.
def test_comparar_fechas_falla_con_formato_incorrecto():
    assert not comparar_fechas("2024-01-10", "2024/01/11")
    assert not comparar_fechas("", "02/01/2024")

 # Prueba de fallo 3: detecta formatos incorrectos.
def test_es_fecha_valida_falla_con_formato_incorrecto():  
    assert not es_fecha_valida("10-10-2025")
    assert not es_fecha_valida("12-2-2025")
    assert not es_fecha_valida("2025/12/01")
