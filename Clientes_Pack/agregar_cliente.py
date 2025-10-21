"""Alta de clientes con validaciones y asignacion automatica de ID."""

from Clientes_Pack.lista_clientes import clientes
from Clientes_Pack.funciones_aux import (
    validar_nombre,
    validar_dni,
    validar_email,
    buscar_indice_por_dni,
)


def generar_nuevo_id():
    """Devuelve el siguiente ID disponible para un cliente."""
    if not clientes:
        return 1
    return max(cliente.get("id", 0) for cliente in clientes) + 1


def agregar_cliente():
    print("\n=== AGREGAR CLIENTE ===")
    nombre = input("Ingrese el nombre completo del cliente: ").strip()
    while not validar_nombre(nombre):
        print("Nombre invalido. Debe tener al menos 3 letras y solo contiene letras o espacios.")
        nombre = input("Ingrese el nombre completo del cliente: ").strip()

    dni = input("Ingrese el DNI del cliente (8 digitos): ").strip()
    while not validar_dni(dni):
        print("DNI invalido. Debe contener exactamente 8 digitos.")
        dni = input("Ingrese el DNI del cliente (8 digitos): ").strip()

    if buscar_indice_por_dni(clientes, dni) != -1:
        print("Ya existe un cliente con ese DNI.")
        return

    email = input("Ingrese el email del cliente: ").strip()
    while not validar_email(email):
        print("Email invalido. Formato esperado ejemplo@dominio.com")
        email = input("Ingrese el email del cliente: ").strip()

    nuevo_id = generar_nuevo_id()
    clientes.append(
        {
            "id": nuevo_id,
            "nombre": nombre,
            "dni": dni,
            "email": email,
            "estado": "activo",
        }
    )
    print(f"Cliente {nombre} agregado con exito. ID: {nuevo_id}")
