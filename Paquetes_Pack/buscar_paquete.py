"""Buscador interactivo de paquetes turisticos."""

from Paquetes_Pack.lista_paquetes import paquetes
from Paquetes_Pack.funciones_aux import (
    ordenar_paquetes,
    buscar_indice_por_id,
    buscar_paquete_por_destino,
)
from Paquetes_Pack.mostrar_paquetes import mostrar_detalle_paquete
from Paquetes_Pack.funciones_aux import mostrar_error, es_numero_positivo


def buscar_paquete():
    while True:
        print("\n=== BUSCAR PAQUETE ===")
        print("1. Por ID")
        print("2. Por destino")
        print("3. Por rango de precio")
        print("0. Volver")
        opcion = input("Opcion: ").strip()

        if opcion == "0":
            return
        elif opcion == "1":
            buscar_por_id()
        elif opcion == "2":
            buscar_por_destino()
        elif opcion == "3":
            buscar_por_precio()
        else:
            mostrar_error("Opcion invalida.")


def buscar_por_id():
    id_txt = input("Ingrese el ID del paquete: ").strip()
    if not id_txt.isdigit():
        mostrar_error("El ID debe ser un numero positivo.")
        return
    indice = buscar_indice_por_id(paquetes, int(id_txt))
    if indice == -1:
        mostrar_error("No se encontro un paquete con ese ID.")
        return
    mostrar_detalle_paquete(int(id_txt))


def buscar_por_destino():
    destino = input("Ingrese el destino: ").strip()
    if destino == "":
        mostrar_error("Debe ingresar un destino.")
        return
    paquete = buscar_paquete_por_destino(paquetes, destino)
    if not paquete:
        mostrar_error("No se encontro un paquete con ese destino.")
        return
    mostrar_detalle_paquete(paquete["id_paquete"])


def buscar_por_precio():
    minimo_txt = input("Precio minimo: ").strip()
    maximo_txt = input("Precio maximo: ").strip()

    if minimo_txt and not es_numero_positivo(minimo_txt):
        mostrar_error("El minimo debe ser un numero positivo.")
        return
    if maximo_txt and not es_numero_positivo(maximo_txt):
        mostrar_error("El maximo debe ser un numero positivo.")
        return

    minimo = int(minimo_txt) if minimo_txt else 0
    maximo = int(maximo_txt) if maximo_txt else None

    coincidencias = []
    for paquete in paquetes:
        precio = int(paquete.get("precio", 0))
        if precio < minimo:
            continue
        if maximo is not None and precio > maximo:
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
    for paquete in coincidencias:
        print(f"{paquete['id_paquete']:<4} | {paquete['destino']:<20} | ${paquete['precio']:>9}")

    opcion = input("\nIngrese un ID para ver el detalle (Enter para omitir): ").strip()
    if opcion:
        if opcion.isdigit():
            mostrar_detalle_paquete(int(opcion))
        else:
            mostrar_error("ID invalido.")
