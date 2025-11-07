# Funciones auxiliares para el manejo de clientes.
import json
import re
# Ruta del archivo JSON donde se almacenan los paquetes.
ARCHIVO_PAQUETES = "Paquetes_Pack/paquetes.json"

# Guarda la lista de paquetes en el archivo JSON.
def guardar_paquete_en_archivo(paquetes):
    try:
        with open(ARCHIVO_PAQUETES, "w", encoding="utf-8") as archivo:
            json.dump(paquetes, archivo, ensure_ascii=False, indent=4)
        return True
    # Si ocurre un error al guardar el archivo, se maneja la excepcion
    except OSError as error:
        print(f"No se pudo guardar el archivo de paquetes: {error}")
        return False

# Carga los clientes desde el archivo JSON.
def cargar_clientes_desde_archivo():
    # Intenta abrir y leer el archivo JSON
    try:
        with open(ARCHIVO_PAQUETES, "r", encoding="utf-8-sig") as archivo:
            datos = json.load(archivo)
            if isinstance(datos, list):
                return datos
            print("Advertencia: el archivo de paquetes tiene un formato invalido.")
    # Maneja errores comunes al abrir o leer el archivo
    except FileNotFoundError:
        guardar_paquete_en_archivo([])
    except json.JSONDecodeError:
        print("Advertencia: no se pudo leer paquetes.json. Se usara una lista vacia.")
    except OSError as error:
        print(f"No se pudo abrir paquetes.json: {error}")
    return []
