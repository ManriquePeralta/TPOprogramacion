from Paquetes_Pack.lista_paquetes import paquetes
from Paquetes_Pack.mostrar_paquetes import mostrar_paquetes
from Paquetes_Pack.validaciones_paquete import es_fecha_valida, es_numero_positivo, mostrar_error

def modificar_paquete():
    mostrar_paquetes()
    destino_buscar = input("Ingrese el destino del paquete a modificar: ")
    for p in paquetes:
        if p["destino"].lower() == destino_buscar.lower():
            print("Deje vacío para no modificar el campo.")
            destino = input(f"Destino actual ({p['destino']}): ").strip() or p['destino']
            if destino == "":
                mostrar_error("El destino no puede estar vacío.")
                return
            precio = input(f"Precio actual ({p['precio']}): ").strip() or str(p['precio'])
            if not es_numero_positivo(precio):
                mostrar_error("El precio debe ser un número positivo.")
                return
            fecha_inicio = input(f"Fecha inicio actual ({p['fecha_inicio']}): ").strip() or p['fecha_inicio']
            fecha_fin = input(f"Fecha fin actual ({p['fecha_fin']}): ").strip() or p['fecha_fin']
            if not es_fecha_valida(fecha_inicio) or not es_fecha_valida(fecha_fin):
                mostrar_error("Las fechas deben tener el formato dd/mm/yyyy y solo números.")
                return
            if fecha_inicio == "" or fecha_fin == "":
                mostrar_error("Las fechas no pueden estar vacías.")
                return
            if fecha_inicio > fecha_fin:
                mostrar_error("La fecha de inicio no puede ser posterior a la de finalización.")
                return
            cupos = input(f"Cupos actual ({p['cupos']}): ").strip() or str(p['cupos'])
            if not es_numero_positivo(cupos):
                mostrar_error("Los cupos deben ser un número positivo.")
                return
            tipo = input(f"Tipo actual ({p['tipo']}): ").strip() or p['tipo']
            descripcion = input(f"Descripción actual ({p['descripcion']}): ").strip() or p['descripcion']
            p['destino'] = destino
            p['precio'] = int(precio)
            p['fecha_inicio'] = fecha_inicio
            p['fecha_fin'] = fecha_fin
            p['cupos'] = int(cupos)
            p['tipo'] = tipo
            p['descripcion'] = descripcion
            print("✅ Paquete modificado.")
            return
    print(" Destino no encontrado.")