# importar funciones auxiliares necesarias
from Clientes_Pack.funciones_aux import (
    validar_nombre,
    validar_dni,
    validar_email,
    buscar_indice_por_dni,
    cargar_clientes_desde_archivo,
    guardar_clientes_en_archivo,
)

# Genera un nuevo ID unico para un cliente.
def generar_nuevo_id(lista_clientes):
    if not lista_clientes:
        return 1
    return max(cliente.get("id", 0) for cliente in lista_clientes) + 1

# Agrega un nuevo cliente al sistema.
def agregar_cliente():
    print("\n=== AGREGAR CLIENTE ===")
    # Carga los clientes actuales
    clientes = cargar_clientes_desde_archivo()
    # Genera un nuevo ID unico
    nuevo_id = generar_nuevo_id(clientes)
    # Solicita nombre del cliente y valida
    nombre = input("Ingrese el nombre completo del cliente: ").strip()
    while not validar_nombre(nombre):
        print("Nombre invalido. Debe tener al menos 3 letras y solo contiene letras o espacios.")
        nombre = input("Ingrese el nombre completo del cliente: ").strip()
    # Solicita DNI del cliente y valida
    dni = input("Ingrese el DNI del cliente (8 digitos): ").strip()
    while not validar_dni(dni):
        print("DNI invalido. Debe contener exactamente 8 digitos.")
        dni = input("Ingrese el DNI del cliente (8 digitos): ").strip()
    # Verifica que el DNI no exista ya
    if buscar_indice_por_dni(clientes, dni) != -1:
        print("Ya existe un cliente con ese DNI.")
        return
    # Solicita email del cliente y valida
    email = input("Ingrese el email del cliente: ").strip()
    while not validar_email(email):
        print("Email invalido. Formato esperado ejemplo@dominio.com")
        email = input("Ingrese el email del cliente: ").strip()
    # Crea el nuevo cliente y lo agrega a la lista
    clientes.append(
        {
            "id": nuevo_id,
            "nombre": nombre,
            "dni": dni,
            "email": email,
            "estado": "activo",
        }
    )
    # Guarda la lista actualizada en el archivo
    if guardar_clientes_en_archivo(clientes):
        print(f"Cliente {nombre} agregado con exito. ID: {nuevo_id}")
    else:
        print("No se pudo guardar el nuevo cliente. Intente nuevamente.")
