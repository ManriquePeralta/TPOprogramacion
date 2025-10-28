# Funciones auxiliares para el manejo de clientes.
import json
import re
# Ruta del archivo JSON donde se almacenan los clientes.
ARCHIVO_CLIENTES = "Clientes_Pack/clientes.json"

# Guarda la lista de clientes en el archivo JSON.
def guardar_clientes_en_archivo(clientes):
    try:
        with open(ARCHIVO_CLIENTES, "w", encoding="utf-8") as archivo:
            json.dump(clientes, archivo, ensure_ascii=False, indent=4)
        return True
    # Si ocurre un error al guardar el archivo, se maneja la excepcion
    except OSError as error:
        print(f"No se pudo guardar el archivo de clientes: {error}")
        return False

# Carga los clientes desde el archivo JSON.
def cargar_clientes_desde_archivo():
    # Intenta abrir y leer el archivo JSON
    try:
        with open(ARCHIVO_CLIENTES, "r", encoding="utf-8-sig") as archivo:
            datos = json.load(archivo)
            if isinstance(datos, list):
                return datos
            print("Advertencia: el archivo de clientes tiene un formato invalido.")
    # Maneja errores comunes al abrir o leer el archivo
    except FileNotFoundError:
        guardar_clientes_en_archivo([])
    except json.JSONDecodeError:
        print("Advertencia: no se pudo leer clientes.json. Se usara una lista vacia.")
    except OSError as error:
        print(f"No se pudo abrir clientes.json: {error}")
    return []

# Normaliza y formatea estados de clientes.
def normalizar_estado(estado):
    return estado.strip().lower()

# Formatea el estado para su presentacion.
def formatear_estado(estado):
    return normalizar_estado(estado).capitalize()

# Ordena la lista de clientes por la clave especificada.
def ordenar_clientes(clientes, clave="id"):
    return sorted(clientes, key=lambda cliente: cliente.get(clave))

# Busca el indice del cliente por su ID. Devuelve -1 si no existe.
def buscar_indice_por_id(clientes, id_cliente):
    indices = {
        clientes[indice].get("id"): indice
        for indice in range(len(clientes))
    }
    return indices.get(id_cliente, -1)

# Busca el indice del cliente por su DNI. Devuelve -1 si no existe.
def buscar_indice_por_dni(clientes, dni):
    indices = {
        clientes[indice].get("dni"): indice
        for indice in range(len(clientes))
    }
    return indices.get(dni, -1)

# Valida que el texto represente un ID numerico positivo.
def validar_id(texto):
    return bool(re.match(r"^\d+$", texto or ""))

# Valida que el DNI tenga exactamente 8 digitos.
def validar_dni(texto):
    return bool(re.match(r"^\d{8}$", texto or ""))

# Valida que el nombre tenga letras y espacios, con longitud minima.
def validar_nombre(nombre):
    if len(nombre.strip()) < 3:
        return False
    # Valida que el nombre solo contenga letras y espacios.
    patron = r"^[A-Za-z\u00C1\u00C9\u00CD\u00D3\u00DA\u00E1\u00E9\u00ED\u00F3\u00FA\u00F1\u00D1 ]+$"
    return bool(re.match(patron, nombre.strip()))

# Valida que el email tenga un formato basico correcto.
def validar_email(email):
    patron = r"^[\w\.-]+@[\w\.-]+\.[A-Za-z]{2,}$"
    return bool(re.match(patron, email.strip()))

# Cuenta cuantos clientes hay por cada estado.
def contar_por_estado(clientes):
    conteo = {}
    for cliente in clientes:
        estado = normalizar_estado(cliente.get("estado", ""))
        conteo[estado] = conteo.get(estado, 0) + 1
    return conteo

# Filtra clientes por estado especifico.
def clientes_por_estado(clientes, estado_buscado):
    estado_buscado = normalizar_estado(estado_buscado)
    return [cliente for cliente in clientes if normalizar_estado(cliente.get("estado", "")) == estado_buscado]

# Obtiene las reservas asociadas a un cliente dado su ID.
def obtener_reservas_de_cliente(reservas, id_cliente):
    coincidencias = []
    # Recorre todas las reservas buscando las que coinciden con el ID del cliente
    for reserva in reservas:
        if type(reserva) is dict:
            if reserva.get("id_cliente") == id_cliente:
                coincidencias.append(reserva)
        elif len(reserva) > 1 and reserva[1] == id_cliente:
            coincidencias.append(reserva)
    return coincidencias

# Obtiene un resumen del conteo de clientes por estado.
def resumen_estados(clientes):
    total = len(clientes)
    conteo = contar_por_estado(clientes)
    activos = conteo.get("activo", 0)
    inactivos = conteo.get("inactivo", 0)
    otros = total - activos - inactivos
    return total, activos, inactivos, otros
