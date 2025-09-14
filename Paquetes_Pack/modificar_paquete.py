from Paquetes_Pack.lista_paquetes import paquetes
from Paquetes_Pack.mostrar_paquetes import mostrar_paquetes
from Paquetes_Pack.validaciones_paquete import es_fecha_valida, es_numero_positivo, mostrar_error

def modificar_paquete():
    id_paquete_txt = input("Ingrese el ID del paquete a modificar: ").strip()
    if not id_paquete_txt.isdigit():
        mostrar_error("El ID debe ser un número positivo.")
        return

    id_paquete = int(id_paquete_txt)
    paquete = next((p for p in paquetes if p["id_paquete"] == id_paquete), None)

    if not paquete:
        print("ID de paquete no encontrado.")
        return

    print("Deje vacío para no modificar el campo.")
    destino = input(f"Destino actual ({paquete['destino']}): ").strip() or paquete['destino']
    if destino == "":
        mostrar_error("El destino no puede estar vacío.")
        return
    precio = input(f"Precio actual ({paquete['precio']}): ").strip() or str(paquete['precio'])
    if not es_numero_positivo(precio):
        mostrar_error("El precio debe ser un número positivo.")
        return
    fecha_inicio = input(f"Fecha inicio actual ({paquete['fecha_inicio']}): ").strip() or paquete['fecha_inicio']
    fecha_fin = input(f"Fecha fin actual ({paquete['fecha_fin']}): ").strip() or paquete['fecha_fin']
    if not es_fecha_valida(fecha_inicio) or not es_fecha_valida(fecha_fin):
        mostrar_error("Las fechas deben tener el formato dd/mm/yyyy y solo números.")
        return
    if fecha_inicio == "" or fecha_fin == "":
        mostrar_error("Las fechas no pueden estar vacías.")
        return
    if fecha_inicio > fecha_fin:
        mostrar_error("La fecha de inicio no puede ser posterior a la de finalización.")
        return
    cupos = input(f"Cupos actual ({paquete['cupos']}): ").strip() or str(paquete['cupos'])
    if not es_numero_positivo(cupos):
        mostrar_error("Los cupos deben ser un número positivo.")
        return
    tipo = input(f"Tipo actual ({paquete['tipo']}): ").strip() or paquete['tipo']
    descripcion = input(f"Descripción actual ({paquete['descripcion']}): ").strip() or paquete['descripcion']

    paquete['destino'] = destino
    paquete['precio'] = int(precio)
    paquete['fecha_inicio'] = fecha_inicio
    paquete['fecha_fin'] = fecha_fin
    paquete['cupos'] = int(cupos)
    paquete['tipo'] = tipo
    paquete['descripcion'] = descripcion

    print("✅ Paquete modificado.")