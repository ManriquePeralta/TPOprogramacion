"""
Módulo para eliminar paquetes turísticos de la lista global.
Permite buscar por destino y elimina el paquete si existe.
"""

# Importación de la lista de paquetes y funciones auxiliares
from Paquetes_Pack.lista_paquetes import paquetes
from Paquetes_Pack.mostrar_paquetes import mostrar_paquetes
from Paquetes_Pack.validaciones_paquete import mostrar_error

def eliminar_paquete():
    # Función que permite eliminar un paquete por destino
    mostrar_paquetes()
    id_buscar = input("\n\nIngrese el ID del paquete a eliminar (0 para salir): ").strip()
    if id_buscar == "0":
        print("Saliendo sin eliminar ningún paquete.")
        return
    if not id_buscar.isdigit():
        mostrar_error("El ID debe ser un número válido.")
        return
    id_buscar = int(id_buscar)
    for p in paquetes:
        if p["id_paquete"] == id_buscar:
            paquetes.remove(p)
            print("✅ Paquete eliminado.")
            return
    mostrar_error("ID no encontrado.")