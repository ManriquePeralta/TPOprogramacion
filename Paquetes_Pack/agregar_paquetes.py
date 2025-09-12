from Paquetes_Pack.lista_paquetes import paquetes
from Paquetes_Pack.validaciones_paquete import es_fecha_valida, es_numero_positivo, mostrar_error
def agregar_paquete():
    print("\n=== AGREGAR PAQUETE ===")
    destino = input("Destino: ").strip()
    if destino == "":
        mostrar_error("El destino no puede estar vacío.")
        return
    precio = input("Precio: ").strip()
    if not es_numero_positivo(precio):
        mostrar_error("El precio debe ser un número positivo.")
        return
    fecha_inicio = input("Fecha inicio (dd/mm/yyyy): ").strip()
    fecha_fin = input("Fecha fin (dd/mm/yyyy): ").strip()
    if not es_fecha_valida(fecha_inicio) or not es_fecha_valida(fecha_fin):
        mostrar_error("Las fechas deben tener el formato dd/mm/yyyy y solo números.")
        return
    if fecha_inicio == "" or fecha_fin == "":
        mostrar_error("Las fechas no pueden estar vacías.")
        return
    if fecha_inicio > fecha_fin:
        mostrar_error("La fecha de finalizacion no puede ser anterior a la de inicio.")
        return
    cupos = input("Cupos: ").strip()
    if not es_numero_positivo(cupos):
        mostrar_error("Los cupos deben ser un número positivo.")
        return
    tipo = input("Tipo: ").strip()
    descripcion = input("Descripción: ").strip()
    paquete = {
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