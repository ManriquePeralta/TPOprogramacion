# Buscador interactivo de paquetes turisticos.

from Paquetes_Pack.funciones_aux import (
    ordenar_paquetes,
    buscar_indice_por_id,
    buscar_paquete_por_destino,
    mostrar_error,
    es_numero_positivo,
    cargar_paquete_desde_archivo,
)
from Paquetes_Pack.mostrar_paquetes import mostrar_detalle_paquete


def buscar_paquete():
    # Despliega el menu de busqueda y ejecuta el filtro elegido.
    while True:
        # Carga la lista actual en cada iteracion para asegurar datos al dia.
        paquetes = cargar_paquete_desde_archivo()
        print("\n=== BUSCAR PAQUETE ===")
        print("1. Por ID")
        print("2. Por destino")
        print("3. Por rango de precio")
        print("0. Volver")
        opcion = input("Opcion: ").strip()

        if opcion == "0":
            return
        if opcion == "1":
            # Ubica el paquete mediante su identificador numerico.
            buscar_por_id(paquetes)
        elif opcion == "2":
            # Localiza destinos exactos registrados.
            buscar_por_destino(paquetes)
        elif opcion == "3":
            # Analiza precios dentro de un rango determinado.
            buscar_por_precio(paquetes)
        else:
            mostrar_error("Opcion invalida.")


def buscar_por_id(paquetes):
    # Busca un paquete a partir de su identificador numerico.
    id_paquete = input("Ingrese el ID del paquete: ").strip()
    if not id_paquete.isdigit():
        mostrar_error("El ID debe ser un numero positivo.")
        return
    indice = buscar_indice_por_id(paquetes, int(id_paquete))
    if indice == -1:
        mostrar_error("No se encontro un paquete con ese ID.")
        return
    mostrar_detalle_paquete(int(id_paquete))


def buscar_por_destino(paquetes):
    # Localiza un paquete segun el destino exacto ingresado.
    destino = input("Ingrese el destino: ").strip()
    if destino == "":
        mostrar_error("Debe ingresar un destino.")
        return
    paquete = buscar_paquete_por_destino(paquetes, destino)
    if paquete is None:
        mostrar_error("No se encontro un paquete con ese destino.")
        return
    # Muestra el detalle del paquete encontrado.
    mostrar_detalle_paquete(paquete["id_paquete"])


def buscar_por_precio(paquetes):
    # Filtra paquetes dentro de un rango de precios solicitado.
    precio_minimo = input("Precio minimo: ").strip()
    precio_maximo = input("Precio maximo: ").strip()

    tiene_minimo = precio_minimo != ""
    tiene_maximo = precio_maximo != ""

    if tiene_minimo and not es_numero_positivo(precio_minimo):
        mostrar_error("El minimo debe ser un numero positivo.")
        return
    if tiene_maximo and not es_numero_positivo(precio_maximo):
        mostrar_error("El maximo debe ser un numero positivo.")
        return

    minimo = int(precio_minimo) if tiene_minimo else 0
    maximo = int(precio_maximo) if tiene_maximo else 0

    # Recorre la lista construyendo la lista de coincidencias.
    coincidencias = []
    for paquete in paquetes:
        precio = int(paquete.get("precio", 0))
        if precio < minimo:
            continue
        if tiene_maximo and precio > maximo:
            continue
        coincidencias.append(paquete)

    if not coincidencias:
        mostrar_error("No se encontraron paquetes en ese rango de precio.")
        return

    coincidencias = ordenar_paquetes(coincidencias)
    encabezado = f"{'ID':<4} | {'Destino':<20} | {'Precio':>10}"
    print("\nPaquetes encontrados:")
    print(encabezado)
    print("-" * len(encabezado))
    # Imprime los paquetes que coinciden con el criterio.
    for paquete in coincidencias:
        print(f"{paquete['id_paquete']:<4} | {paquete['destino']:<20} | ${paquete['precio']:>9}")

    opcion = input("\nIngrese un ID para ver el detalle (Enter para omitir): ").strip()
    if opcion and opcion.isdigit():
        mostrar_detalle_paquete(int(opcion))
    elif opcion:
        mostrar_error("ID invalido.")
