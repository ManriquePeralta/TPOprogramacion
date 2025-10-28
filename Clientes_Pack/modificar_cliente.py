# Modificacion de datos de clientes con validaciones adicionales.

from Clientes_Pack.funciones_aux import (
    validar_id,
    validar_nombre,
    validar_dni,
    validar_email,
    buscar_indice_por_id,
    buscar_indice_por_dni,
    normalizar_estado,
    formatear_estado,
    cargar_clientes_desde_archivo,
    guardar_clientes_en_archivo,
)
from Clientes_Pack.mostrar_cliente import mostrar_clientes

# Modifica los datos de un cliente existente.
def modificar_cliente():
    print("\n=== MODIFICAR CLIENTE ===")

    # Muestra el listado de clientes
    listado = mostrar_clientes()
    if not listado:
        return
    
    # Carga los clientes actuales
    clientes_actuales = cargar_clientes_desde_archivo()

    # Solicita el ID del cliente a modificar y valida
    id_cliente = input("\nIngrese el ID del cliente a modificar (0 para salir): ").strip()
    while not validar_id(id_cliente):
        if id_cliente == "0":
            print("Operacion cancelada. No se modifico ningun cliente.")
            return
        print("ID invalido. Debe ser un numero positivo.")
        id_cliente = input("Ingrese el ID del cliente a modificar (0 para salir): ").strip()
    if id_cliente == "0":
        print("Operacion cancelada. No se modifico ningun cliente.")
        return
    
    # Convierte el ID a entero y busca el cliente
    id_cliente = int(id_cliente)
    indice = buscar_indice_por_id(clientes_actuales, id_cliente)
    if indice == -1:
        print(f"No se encontro un cliente con ID {id_cliente}.")
        return
   
    # Obtiene el cliente a modificar
    cliente = clientes_actuales[indice]
    print(f"Cliente seleccionado: {cliente['nombre']} (Estado actual: {formatear_estado(cliente['estado'])})")
   
    # Actualiza los campos del cliente
    actualizar_nombre(cliente)
    actualizar_dni(clientes_actuales, cliente, indice)
    actualizar_email(cliente)
    actualizar_estado(cliente)

    # Guarda los cambios en el archivo
    if guardar_clientes_en_archivo(clientes_actuales):
        print(f"Cliente ID {id_cliente} actualizado correctamente.")
    else:
        print("No se pudieron guardar los cambios del cliente.")

# Actualiza el nombre del cliente 
def actualizar_nombre(cliente):
    # solicita el nuevo nombre y valida
    nuevo_nombre = input("Nuevo nombre (dejar vacio para mantener): ").strip()
    while nuevo_nombre and not validar_nombre(nuevo_nombre):
        print("Nombre invalido. Debe tener al menos 3 letras y solo letras o espacios.")
        nuevo_nombre = input("Nuevo nombre (dejar vacio para mantener): ").strip()
    if nuevo_nombre:
        cliente["nombre"] = nuevo_nombre

# Actualiza el DNI del cliente 
def actualizar_dni(clientes, cliente, posicion_actual):
    # solicita el nuevo DNI y valida
    nuevo_dni = input("Nuevo DNI (dejar vacio para mantener): ").strip()
    while nuevo_dni and not validar_dni(nuevo_dni):
        print("DNI invalido. Debe contener exactamente 8 digitos.")
        nuevo_dni = input("Nuevo DNI (dejar vacio para mantener): ").strip()
    # Verifica si se dejo el campo vacio
    if not nuevo_dni:
        return
    # Verifica que el DNI no esté en uso por otro cliente
    indice_dni = buscar_indice_por_dni(clientes, nuevo_dni)
    if indice_dni != -1 and indice_dni != posicion_actual:
        print("Ese DNI ya esta asignado a otro cliente. Se mantiene el DNI original.")
        return

    cliente["dni"] = nuevo_dni

# Actualiza el email del cliente
def actualizar_email(cliente):
    # solicita el nuevo email y valida
    nuevo_email = input("Nuevo email (dejar vacio para mantener): ").strip()
    while nuevo_email and not validar_email(nuevo_email):
        print("Email invalido. Formato esperado ejemplo@dominio.com")
        nuevo_email = input("Nuevo email (dejar vacio para mantener): ").strip()
    if nuevo_email:
        cliente["email"] = nuevo_email

# Actualiza el estado del cliente
def actualizar_estado(cliente):
   # solicita el nuevo estado y valida
    nuevo_estado = input("Nuevo estado (Activo/Inactivo) [Enter para mantener]: ").strip()
    while nuevo_estado:
        estado_normalizado = normalizar_estado(nuevo_estado)
        if estado_normalizado in ("activo", "inactivo"):
            cliente["estado"] = estado_normalizado
            return
        print("Estado invalido. Opciones: Activo o Inactivo.")
        nuevo_estado = input("Nuevo estado (Activo/Inactivo) [Enter para mantener]: ").strip()
