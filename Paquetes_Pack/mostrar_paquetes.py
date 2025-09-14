"""
Módulo para mostrar la lista de paquetes turísticos y consultar detalles por ID o destino.
Incluye formato de tabla y validaciones de entrada.
"""

# Importación de la lista de paquetes y función de error
from Paquetes_Pack.lista_paquetes import paquetes
from Paquetes_Pack.validaciones_paquete import mostrar_error
def mostrar_paquetes():
    # Función que muestra la tabla de paquetes
    ancho_destino = 20
    ancho_precio = 10
    ancho_fecha = 12
    ancho_cupos = 8
    ancho_tipo = 10
    ancho_desc = 40

    ancho_id = 5
    print(f'{"ID":<{ancho_id}} {"Destino":<{ancho_destino}} {"Precio":>{ancho_precio}} {"Desde":^{ancho_fecha}} {"Hasta":^{ancho_fecha}} {"Cupos":>{ancho_cupos}} {"Tipo":<{ancho_tipo}} {"Descripcion":<{ancho_desc}}')
    print("-" * (ancho_id + ancho_destino + ancho_precio + 2 * ancho_fecha + ancho_cupos + ancho_tipo + ancho_desc + 7))

    if not paquetes:
        mostrar_error("No hay paquetes disponibles.")
        return
    # Filas
    for paquete in paquetes:
        print(f'{paquete["id_paquete"]:<{ancho_id}} {paquete["destino"]:<{ancho_destino}} ${paquete["precio"]:>{ancho_precio - 1}} {paquete["fecha_inicio"]:^{ancho_fecha}} {paquete["fecha_fin"]:^{ancho_fecha}} {paquete["cupos"]:>{ancho_cupos}} {paquete["tipo"]:<{ancho_tipo}} {paquete["descripcion"]:<{ancho_desc}}')

def buscar_detalle_paquete():
    # Función que permite buscar detalles de un paquete
    print("\n¿Desea ver el detalle de un paquete?")
    print("1. Buscar por ID")
    print("2. Buscar por destino")
    opcion = input("Seleccione opción (1/2, Enter para salir): ").strip()
    if opcion == "1":
        id_txt = input("Ingrese el ID del paquete: ").strip()
        if not id_txt.isdigit():
            mostrar_error("ID inválido.")
            return
        id_buscar = int(id_txt)
        paquete = next((p for p in paquetes if p["id_paquete"] == id_buscar), None)
        if paquete:
            print("\n=== DETALLE DEL PAQUETE ===")
            for k, v in paquete.items():
                print(f"{k.capitalize()}: {v}")
        else:
            mostrar_error("ID no encontrado.")
    elif opcion == "2":
        destino_buscar = input("Ingrese el destino del paquete: ").strip().lower()
        paquete = next((p for p in paquetes if p["destino"].lower() == destino_buscar), None)
        if paquete:
            print("\n=== DETALLE DEL PAQUETE ===")
            for k, v in paquete.items():
                print(f"{k.capitalize()}: {v}")
        else:
            mostrar_error("Destino no encontrado.")
