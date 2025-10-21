"""Buscador interactivo de clientes por distintos criterios."""

from Clientes_Pack.lista_clientes import clientes
from Clientes_Pack.funciones_aux import (
    validar_id,
    validar_dni,
    ordenar_clientes,
    buscar_indice_por_id,
    buscar_indice_por_dni,
)
from Clientes_Pack.mostrar_cliente import mostrar_detalle_cliente


def buscar_cliente():
    while True:
        print("\n=== BUSCAR CLIENTE ===")
        print("1. Por ID")
        print("2. Por DNI")
        print("3. Por nombre (coincidencia parcial)")
        print("0. Volver")
        opcion = input("Opcion: ").strip()

        if opcion == "0":
            return
        elif opcion == "1":
            buscar_por_id()
        elif opcion == "2":
            buscar_por_dni()
        elif opcion == "3":
            buscar_por_nombre()
        else:
            print("Opcion invalida.")


def buscar_por_id():
    id_txt = input("Ingrese el ID del cliente: ").strip()
    if not validar_id(id_txt):
        print("ID invalido. Debe ser numerico.")
        return
    indice = buscar_indice_por_id(clientes, int(id_txt))
    if indice == -1:
        print("No se encontro un cliente con ese ID.")
        return
    mostrar_detalle_cliente(int(id_txt))


def buscar_por_dni():
    dni = input("Ingrese el DNI (8 digitos): ").strip()
    if not validar_dni(dni):
        print("DNI invalido. Debe tener exactamente 8 digitos.")
        return
    indice = buscar_indice_por_dni(clientes, dni)
    if indice == -1:
        print("No se encontro un cliente con ese DNI.")
        return
    mostrar_detalle_cliente(clientes[indice]["id"])


def buscar_por_nombre():
    termino = input("Ingrese parte del nombre a buscar: ").strip().lower()
    if not termino:
        print("Debe ingresar al menos una letra.")
        return
    coincidencias = [c for c in clientes if termino in c["nombre"].lower()]
    if not coincidencias:
        print("No se encontraron coincidencias con ese nombre.")
        return

    coincidencias = ordenar_clientes(coincidencias, "nombre")
    encabezado = f"{'ID':<4} | {'Nombre':<22} | {'DNI':<10}"
    print("\nCoincidencias encontradas:")
    print(encabezado)
    print("-" * len(encabezado))
    for cliente in coincidencias:
        print(f"{cliente['id']:<4} | {cliente['nombre']:<22} | {cliente['dni']:<10}")

    opcion = input("\nIngrese un ID para ver el detalle (Enter para omitir): ").strip()
    if opcion:
        if validar_id(opcion):
            mostrar_detalle_cliente(int(opcion))
        else:
            print("ID invalido. Se omite la visualizacion del detalle.")
