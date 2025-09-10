from Paquetes_Pack.lista_paquetes import paquetes
from Paquetes_Pack.mostrar_paquetes import mostrar_paquetes

def eliminar_paquete():
    mostrar_paquetes()
    destino_buscar = input("Ingrese el destino del paquete a eliminar: ").strip()
    if destino_buscar == "":
        print(" El destino no puede estar vacío.")
        return
    for p in paquetes:
        if p["destino"].lower() == destino_buscar.lower():
            paquetes.remove(p)
            print("✅ Paquete eliminado.")
            return
    print("Destino no encontrado.")