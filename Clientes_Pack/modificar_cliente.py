"""Modificacion de datos de clientes con validaciones adicionales."""

from Clientes_Pack.lista_clientes import clientes
from Clientes_Pack.funciones_aux import (
    validar_id,
    validar_nombre,
    validar_dni,
    validar_email,
    buscar_indice_por_id,
    buscar_indice_por_dni,
    normalizar_estado,
    formatear_estado,
)
from Clientes_Pack.mostrar_cliente import mostrar_clientes

ESTADOS_PERMITIDOS = ["activo", "inactivo", "suspendido"]


def modificar_cliente():
    print("\n=== MODIFICAR CLIENTE ===")
    listado = mostrar_clientes(interactivo=False)
    if not listado:
        return

    id_cliente_txt = input("\nIngrese el ID del cliente a modificar (0 para salir): ").strip()

    if id_cliente_txt == "0":
        print("Operacion cancelada. No se modifico ningun cliente.")
        return

    while not validar_id(id_cliente_txt):
        print("ID invalido. Debe ser un numero positivo.")
        id_cliente_txt = input("Ingrese el ID del cliente a modificar (0 para salir): ").strip()
        if id_cliente_txt == "0":
            print("Operacion cancelada. No se modifico ningun cliente.")
            return

    id_cliente = int(id_cliente_txt)
    indice = buscar_indice_por_id(clientes, id_cliente)

    if indice == -1:
        print(f"No se encontro un cliente con ID {id_cliente}.")
        return

    cliente = clientes[indice]
    print(f"Cliente seleccionado: {cliente['nombre']} (Estado actual: {formatear_estado(cliente['estado'])})")

    nuevo_nombre = input("Nuevo nombre (dejar vacio para mantener): ").strip()
    if nuevo_nombre:
        while not validar_nombre(nuevo_nombre):
            print("Nombre invalido. Debe tener al menos 3 letras y solo contiene letras o espacios.")
            nuevo_nombre = input("Nuevo nombre (dejar vacio para mantener): ").strip()
        cliente["nombre"] = nuevo_nombre

    nuevo_dni = input("Nuevo DNI (dejar vacio para mantener): ").strip()
    if nuevo_dni:
        while not validar_dni(nuevo_dni):
            print("DNI invalido. Debe contener exactamente 8 digitos.")
            nuevo_dni = input("Nuevo DNI (dejar vacio para mantener): ").strip()
            if not nuevo_dni:
                break
        if nuevo_dni:
            indice_dni = buscar_indice_por_dni(clientes, nuevo_dni)
            if indice_dni != -1 and indice_dni != indice:
                print("Ese DNI ya esta asignado a otro cliente. No se realizaron cambios en el DNI.")
            else:
                cliente["dni"] = nuevo_dni

    nuevo_email = input("Nuevo email (dejar vacio para mantener): ").strip()
    if nuevo_email:
        while not validar_email(nuevo_email):
            print("Email invalido. Formato esperado ejemplo@dominio.com")
            nuevo_email = input("Nuevo email (dejar vacio para mantener): ").strip()
            if not nuevo_email:
                break
        if nuevo_email:
            cliente["email"] = nuevo_email

    nuevo_estado = input("Nuevo estado (Activo/Inactivo/Suspendido) [Enter para mantener]: ").strip()
    if nuevo_estado:
        estado_normalizado = normalizar_estado(nuevo_estado)
        while estado_normalizado not in ESTADOS_PERMITIDOS:
            print("Estado invalido. Opciones: Activo, Inactivo o Suspendido.")
            nuevo_estado = input("Nuevo estado (Activo/Inactivo/Suspendido) [Enter para mantener]: ").strip()
            if not nuevo_estado:
                estado_normalizado = None
                break
            estado_normalizado = normalizar_estado(nuevo_estado)
        if estado_normalizado:
            cliente["estado"] = estado_normalizado

    print(f"Cliente ID {id_cliente} actualizado correctamente.")
