from Paquetes_Pack.lista_paquetes import paquetes
from Paquetes_Pack.mostrar_paquetes import mostrar_paquetes

def modificar_paquete():
    mostrar_paquetes()
    destino_buscar = input("Ingrese el destino del paquete a modificar: ")
    for p in paquetes:
        if p[0].lower() == destino_buscar.lower():
            print("Deje vacío para no modificar el campo.")
            destino = input(f"Destino actual ({p[0]}): ").strip() or p[0]
            if destino == "":
                print("❌ El destino no puede estar vacío.")
                return
            precio = input(f"Precio actual ({p[1]}): ").strip() or str(p[1])
            if not precio.isdigit() or int(precio) < 0:
                print("❌ El precio debe ser un número positivo.")
                return
            fecha_inicio = input(f"Fecha inicio actual ({p[2]}): ").strip() or p[2]
            fecha_fin = input(f"Fecha fin actual ({p[3]}): ").strip() or p[3]
            if fecha_inicio == "" or fecha_fin == "":
                print("❌ Las fechas no pueden estar vacías.")
                return
            if fecha_inicio > fecha_fin:
                print("❌ La fecha de inicio no puede ser posterior a la de finalización.")
                return
            cupos = input(f"Cupos actual ({p[4]}): ").strip() or str(p[4])
            if not cupos.isdigit() or int(cupos) < 0:
                print("❌ Los cupos deben ser un número positivo.")
                return
            tipo = input(f"Tipo actual ({p[5]}): ").strip() or p[5]
            descripcion = input(f"Descripción actual ({p[6]}): ").strip() or p[6]
            p[0] = destino
            p[1] = int(precio)
            p[2] = fecha_inicio
            p[3] = fecha_fin
            p[4] = int(cupos)
            p[5] = tipo
            p[6] = descripcion
            print("✅ Paquete modificado.")
            return
    print("❌ Destino no encontrado.")