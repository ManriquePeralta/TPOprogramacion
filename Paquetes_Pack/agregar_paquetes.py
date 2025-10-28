# Alta de paquetes con validaciones y asignacion automatica de ID.

from Paquetes_Pack.funciones_aux import (
    generar_nuevo_id,
    buscar_paquete_por_destino,
    mostrar_error,
    es_numero_positivo,
    es_fecha_valida,
    comparar_fechas,
    cargar_paquete_desde_archivo,
    guardar_paquete_en_archivo,
)
# Definimos los tipos validos de paquetes
TIPOS_VALIDOS = ("Estandar", "Premium", "Full")

# Recolecta los datos del paquete y lo registra en el archivo.
def agregar_paquete():
    print("\n=== AGREGAR PAQUETE ===")
    paquetes = cargar_paquete_desde_archivo()
    # Solicita el destino y valida que no este vacio
    destino = input("Destino: ").strip()
    while not destino:
        mostrar_error("El destino no puede estar vacio.")
        destino = input("Destino: ").strip()
    # Verifica que el destino no exista previamente.
    while buscar_paquete_por_destino(paquetes, destino):
        mostrar_error("Ya existe un paquete con ese destino.")
        destino = input("Destino (otro): ").strip()
        while not destino:
            mostrar_error("El destino no puede estar vacio.")
            destino = input("Destino (otro): ").strip()
    # Solicita el precio y valida que sea positivo.
    precio_txt = input("Precio: ").strip()
    while not es_numero_positivo(precio_txt):
        mostrar_error("El precio debe ser un numero positivo.")
        precio_txt = input("Precio: ").strip()
    # Solicita la fecha de inicio y valida el formato.
    fecha_inicio = input("Fecha inicio (dd/mm/yyyy): ").strip()
    while not es_fecha_valida(fecha_inicio):
        mostrar_error("La fecha debe tener el formato dd/mm/yyyy.")
        fecha_inicio = input("Fecha inicio (dd/mm/yyyy): ").strip()
    # Solicita la fecha de fin y controla que sea posterior al inicio.
    fecha_fin = input("Fecha fin (dd/mm/yyyy): ").strip()
    while not es_fecha_valida(fecha_fin) or not comparar_fechas(fecha_inicio, fecha_fin):
        mostrar_error("La fecha de fin no puede ser anterior a la de inicio.")
        fecha_fin = input("Fecha fin (dd/mm/yyyy): ").strip()
        while not es_fecha_valida(fecha_fin):
            mostrar_error("La fecha debe tener el formato dd/mm/yyyy.")
            fecha_fin = input("Fecha fin (dd/mm/yyyy): ").strip()
    # Solicita los cupos y valida que sea un entero positivo.
    cupos_txt = input("Cupos disponibles: ").strip()
    while not es_numero_positivo(cupos_txt):
        mostrar_error("Los cupos deben ser un numero entero positivo.")
        cupos_txt = input("Cupos disponibles: ").strip()
    # Solicita el tipo de paquete y valida que sea uno permitido.
    tipo = input("Tipo (Estandar/Premium/Full) [Estandar]: ").strip()
    if not tipo:
        tipo = "Estandar"
    tipo_normalizado = tipo.capitalize()
    while tipo_normalizado not in TIPOS_VALIDOS:
        mostrar_error("Tipo invalido. Opciones: Estandar, Premium o Full.")
        tipo = input("Tipo (Estandar/Premium/Full) [Estandar]: ").strip()
        if not tipo:
            tipo = "Estandar"
        tipo_normalizado = tipo.capitalize()
    # Solicita la descripcion y valida que no quede vacia.
    descripcion = input("Descripcion: ").strip()
    while not descripcion:
        mostrar_error("La descripcion no puede estar vacia.")
        descripcion = input("Descripcion: ").strip()
    # Genera el ID y crea el paquete
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
    # Agrega el paquete armado a la lista en memoria.
    paquetes.append(paquete)
    # Guarda el paquete en el archivo
    if guardar_paquete_en_archivo(paquetes):
        print(f"Paquete a {destino} agregado con exito. ID: {paquete['id_paquete']}")
    else: 
        # Si no se pudo guardar, informa el error al usuario.
        mostrar_error("No se pudo guardar el nuevo paquete. Intente nuevamente.")
