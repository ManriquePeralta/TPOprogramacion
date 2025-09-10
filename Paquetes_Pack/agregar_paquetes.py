from Paquetes_Pack.lista_paquetes import paquetes
def agregar_paquete():
    print("\n=== AGREGAR PAQUETE ===")
    destino = input("Destino: ").strip()
    if destino == "":
        print(" El destino no puede estar vacío.")
        return
    precio = input("Precio: ").strip()
    if not precio.isdigit() or int(precio) < 0:
        print(" El precio debe ser un número positivo.")
        return
    import re
    fecha_inicio = input("Fecha inicio (dd/mm/yyyy): ").strip()
    fecha_fin = input("Fecha fin (dd/mm/yyyy): ").strip()
    formato_fecha = r"^\d{2}/\d{2}/\d{4}$"
    if not re.match(formato_fecha, fecha_inicio) or not re.match(formato_fecha, fecha_fin):
        print(" Las fechas deben tener el formato dd/mm/yyyy y solo números.")
        return
    if fecha_inicio == "" or fecha_fin == "":
        print(" Las fechas no pueden estar vacías.")
        return
    if fecha_inicio > fecha_fin:
        print(" La fecha de finalizacion no puede ser anterior a la de inicio.")
        return
    cupos = input("Cupos: ").strip()
    if not cupos.isdigit() or int(cupos) < 0:
        print(" Los cupos deben ser un número positivo.")
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