"""Alta de paquetes con validaciones y asignacion automatica de ID."""

from Paquetes_Pack.lista_paquetes import paquetes
from Paquetes_Pack.funciones_aux import (
    generar_nuevo_id,
    buscar_paquete_por_destino,
    mostrar_error,
    es_numero_positivo,
    es_fecha_valida,
    comparar_fechas,
)


def agregar_paquete():
    print("\n=== AGREGAR PAQUETE ===")

    destino = input("Destino: ").strip()
    if destino == "":
        mostrar_error("El destino no puede estar vacio.")
        return

    if buscar_paquete_por_destino(paquetes, destino):
        mostrar_error("Ya existe un paquete con ese destino.")
        return

    precio_txt = input("Precio: ").strip()
    if not es_numero_positivo(precio_txt):
        mostrar_error("El precio debe ser un numero positivo.")
        return

    fecha_inicio = input("Fecha inicio (dd/mm/yyyy): ").strip()
    fecha_fin = input("Fecha fin (dd/mm/yyyy): ").strip()

    if not es_fecha_valida(fecha_inicio) or not es_fecha_valida(fecha_fin):
        mostrar_error("Las fechas deben tener el formato dd/mm/yyyy.")
        return

    if not comparar_fechas(fecha_inicio, fecha_fin):
        mostrar_error("La fecha de fin no puede ser anterior a la de inicio.")
        return

    cupos_txt = input("Cupos disponibles: ").strip()
    if not es_numero_positivo(cupos_txt):
        mostrar_error("Los cupos deben ser un numero entero positivo.")
        return

    tipo = input("Tipo (Estandar/Premium/Full) [Estandar]: ").strip()
    if tipo == "":
        tipo = "Estandar"
    tipo_normalizado = tipo.capitalize()
    opciones_tipo = ["Estandar", "Premium", "Full"]
    if tipo_normalizado not in opciones_tipo:
        mostrar_error("Tipo invalido. Opciones: Estandar, Premium o Full.")
        return

    descripcion = input("Descripcion: ").strip()
    if descripcion == "":
        mostrar_error("La descripcion no puede estar vacia.")
        return

    nuevo_id = generar_nuevo_id(paquetes)
    paquete = {
        "id_paquete": nuevo_id,
        "destino": destino,
        "precio": int(precio_txt),
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "cupos": int(cupos_txt),
        "tipo": tipo_normalizado,
        "descripcion": descripcion,
    }
    paquetes.append(paquete)

    print(f"Paquete a {destino} agregado con exito. ID: {paquete['id_paquete']}")
