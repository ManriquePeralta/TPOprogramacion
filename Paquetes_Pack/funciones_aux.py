# Funciones auxiliares para la gestion de paquetes.

import json
import re

# Ruta del archivo donde se guardan los paquetes persistidos.
ARCHIVO_PAQUETES = "Paquetes_Pack/paquetes.json"


def mostrar_error(mensaje):
    # Imprime un mensaje de error formateado.
    print(f"{mensaje}")


def normalizar_texto(texto):
    # Devuelve el texto sin espacios extra y en minusculas.
    return texto.strip().lower()


def guardar_paquete_en_archivo(paquetes):
    # Guarda la lista de paquetes en el archivo JSON.
    try:
        with open(ARCHIVO_PAQUETES, "w", encoding="utf-8") as archivo:
            json.dump(paquetes, archivo, ensure_ascii=False, indent=4)
        return True
    except OSError as error:
        print(f"No se pudo guardar el archivo de paquetes: {error}")
        return False


def cargar_paquete_desde_archivo():
    # Carga los paquetes almacenados en el archivo JSON.
    try:
        with open(ARCHIVO_PAQUETES, "r", encoding="utf-8-sig") as archivo:
            datos = json.load(archivo)
            if isinstance(datos, list):
                return datos
            print("Advertencia: el archivo de paquetes tiene un formato invalido.")
    except FileNotFoundError:
        guardar_paquete_en_archivo([])
    except json.JSONDecodeError:
        print("Advertencia: no se pudo leer paquetes.json. Se usara una lista vacia.")
    except OSError as error:
        print(f"No se pudo abrir paquetes.json: {error}")
    return []


def ordenar_paquetes(paquetes, clave="id_paquete"):
    # Ordena una copia de la lista de paquetes segun la clave indicada.
    return sorted(paquetes, key=lambda paquete: paquete.get(clave))


def generar_nuevo_id(paquetes):
    # Calcula el siguiente ID disponible.
    mayor = 0
    for paquete in paquetes:
        mayor = max(mayor, int(paquete.get("id_paquete", 0)))
    return mayor + 1


def buscar_indice_por_id(paquetes, id_paquete):
    # Busca el indice del paquete por ID. Devuelve -1 si no existe.
    indices = {
        paquetes[indice].get("id_paquete"): indice
        for indice in range(len(paquetes))
    }
    return indices.get(id_paquete, -1)


def buscar_paquete_por_destino(paquetes, destino):
    # Devuelve el primer paquete cuyo destino coincide (case insensitive).
    destino = normalizar_texto(destino)
    for paquete in paquetes:
        if normalizar_texto(paquete.get("destino", "")) == destino:
            return paquete
    return None


def paquetes_disponibles(paquetes):
    # Filtra paquetes con cupos mayores a cero.
    return [paquete for paquete in paquetes if int(paquete.get("cupos", 0)) > 0]


def paquetes_sin_cupo(paquetes):
    # Filtra paquetes sin disponibilidad de cupos.
    return [paquete for paquete in paquetes if int(paquete.get("cupos", 0)) == 0]


def conteo_por_tipo(paquetes):
    # Cuenta cuantos paquetes hay por tipo.
    conteo = {}
    for paquete in paquetes:
        tipo = paquete.get("tipo", "Sin tipo")
        conteo[tipo] = conteo.get(tipo, 0) + 1
    return conteo


def conteo_por_destino(paquetes):
    # Cuenta cuantas veces aparece cada destino.
    conteo = {}
    for paquete in paquetes:
        destino = paquete.get("destino", "Destino desconocido")
        conteo[destino] = conteo.get(destino, 0) + 1
    return conteo


def total_cupos(paquetes):
    # Suma los cupos disponibles de todos los paquetes.
    return sum(int(paquete.get("cupos", 0)) for paquete in paquetes)


def promedio_precio(paquetes):
    # Calcula el precio promedio de los paquetes.
    lista = list(paquetes)
    if not lista:
        return 0.0
    return sum(float(paquete.get("precio", 0)) for paquete in lista) / len(lista)


def max_precio(paquetes):
    # Obtiene el precio maximo registrado.
    lista = list(paquetes)
    if not lista:
        return 0.0
    return max(float(paquete.get("precio", 0)) for paquete in lista)


def min_precio(paquetes):
    # Obtiene el precio minimo registrado.
    lista = list(paquetes)
    if not lista:
        return 0.0
    return min(float(paquete.get("precio", 0)) for paquete in lista)


def destinos_unicos(paquetes):
    # Devuelve una lista de destinos sin repetir.
    vistos = {paquete.get("destino", "Destino desconocido") for paquete in paquetes}
    return sorted(vistos)


def es_fecha_valida(fecha):
    # Verifica si la fecha tiene formato dd/mm/yyyy y solo numeros.
    return bool(re.match(r"^\d{2}/\d{2}/\d{4}$", fecha or ""))


def comparar_fechas(fecha_inicio, fecha_fin):
    # Compara dos fechas en formato dd/mm/yyyy y verifica inicio <= fin.
    partes_inicio = fecha_inicio.split("/")
    partes_fin = fecha_fin.split("/")
    if len(partes_inicio) != 3 or len(partes_fin) != 3:
        return False
    dia_i = int(partes_inicio[0])
    mes_i = int(partes_inicio[1])
    anio_i = int(partes_inicio[2])
    dia_f = int(partes_fin[0])
    mes_f = int(partes_fin[1])
    anio_f = int(partes_fin[2])
    if anio_i != anio_f:
        return anio_i < anio_f
    if mes_i != mes_f:
        return mes_i <= mes_f
    return dia_i <= dia_f


def es_numero_positivo(valor):
    # Verifica si el valor es un numero entero positivo.
    return valor.isdigit() and int(valor) >= 0
