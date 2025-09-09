from Paquetes_Pack.lista_paquetes import paquetes
def agregar_paquete():
    print("\n=== AGREGAR PAQUETE ===")
    destino = input("Destino: ").strip()
    if destino == "":
        print("❌ El destino no puede estar vacío.")
        return
    precio = input("Precio: ").strip()
    if not precio.isdigit() or int(precio) < 0:
        print("❌ El precio debe ser un número positivo.")
        return
    fecha_inicio = input("Fecha inicio (dd/mm/yyyy): ").strip()
    fecha_fin = input("Fecha fin (dd/mm/yyyy): ").strip()
    if fecha_inicio == "" or fecha_fin == "":
        print("❌ Las fechas no pueden estar vacías.")
        return
    # Validación simple de fechas (no posterioridad, solo formato y comparación de strings)
    if fecha_inicio > fecha_fin:
        print("❌ La fecha de inicio no puede ser posterior a la de finalización.")
        return
    cupos = input("Cupos: ").strip()
    if not cupos.isdigit() or int(cupos) < 0:
        print("❌ Los cupos deben ser un número positivo.")
        return
    tipo = input("Tipo: ").strip()
    descripcion = input("Descripción: ").strip()
    paquetes.append([destino, int(precio), fecha_inicio, fecha_fin, int(cupos), tipo, descripcion])
    print("✅ Paquete agregado.")