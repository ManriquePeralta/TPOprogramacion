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
    destino_buscar = input("Ingrese el destino del paquete a eliminar: ").strip()
    if destino_buscar == "":
        mostrar_error("El destino no puede estar vacío.")
        return
    for p in paquetes:
        if p["destino"].lower() == destino_buscar.lower():
            paquetes.remove(p)
            print("✅ Paquete eliminado.")
            return
    mostrar_error("Destino no encontrado.")