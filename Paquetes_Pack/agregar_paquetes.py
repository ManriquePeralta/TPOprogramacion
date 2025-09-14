
# Importación de la lista de paquetes y funciones de validación
from Paquetes_Pack.lista_paquetes import paquetes
from Paquetes_Pack.validaciones_paquete import es_fecha_valida, es_numero_positivo, mostrar_error, comparar_fechas


# Esta función permite al usuario agregar un nuevo paquete turístico, validando la entrada y agregando el paquete a la lista global.
def agregar_paquete():
    print("\n=== AGREGAR PAQUETE ===")

    # Solicitar destino y validar que no esté vacío
    destino = input("Destino: ").strip()
    if destino == "":
        mostrar_error("El destino no puede estar vacío.")
        return

    # Solicitar precio y validar que sea un número positivo
    precio = input("Precio: ").strip()
    if not es_numero_positivo(precio):
        mostrar_error("El precio debe ser un número positivo.")
        return

    # Solicitar fechas y validar formato y lógica
    fecha_inicio = input("Fecha inicio (dd/mm/yyyy): ").strip()
    fecha_fin = input("Fecha fin (dd/mm/yyyy): ").strip()
    if not es_fecha_valida(fecha_inicio) or not es_fecha_valida(fecha_fin):
        mostrar_error("Las fechas deben tener el formato dd/mm/yyyy y solo números.")
        return
    if fecha_inicio == "" or fecha_fin == "":
        mostrar_error("Las fechas no pueden estar vacías.")
        return
    if not comparar_fechas(fecha_inicio, fecha_fin):
        mostrar_error("La fecha de finalizacion no puede ser anterior a la de inicio.")
        return

    # Solicitar cupos y validar que sea un número positivo
    cupos = input("Cupos: ").strip()
    if not es_numero_positivo(cupos):
        mostrar_error("Los cupos deben ser un número positivo.")
        return

    # Solicitar tipo y descripción
    tipo = input("Tipo: ").strip()
    descripcion = input("Descripción: ").strip()

    # Crear el diccionario del paquete y agregarlo a la lista global
    paquete = {
        "id_paquete": max([p["id_paquete"] for p in paquetes]) + 1,
        "destino": destino,
        "precio": int(precio),
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "cupos": int(cupos),
        "tipo": tipo,
        "descripcion": descripcion
    }
    paquetes.append(paquete)
    print("✅ Paquete agregado.")