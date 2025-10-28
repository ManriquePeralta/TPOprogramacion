# importa las todas las funciones necesarias
from Clientes_Pack.funciones_aux import (
    validar_id,
    validar_dni,
    buscar_indice_por_id,
    buscar_indice_por_dni,
    cargar_clientes_desde_archivo,
)
from Clientes_Pack.mostrar_cliente import mostrar_detalle_cliente

# Menu para buscar clientes por diferentes criterios.
def buscar_cliente():
   # Permite buscar clientes por ID, DNI o nombre.
    while True:
        # Carga los clientes desde el archivo
        clientes = cargar_clientes_desde_archivo()
        if not clientes:
            print("\nNo hay clientes cargados para buscar.\n")
            return
        # Muestra el menu de opciones
        print("\n=== BUSCAR CLIENTE ===")
        print("1. Por ID")
        print("2. Por DNI")
        print("3. Por nombre (coincidencia parcial)")
        print("0. Volver")
        # Solicita la opcion del usuario
        opcion = input("Opcion: ").strip()
        # Ejecuta la accion correspondiente
        if opcion == "0":
            return
        elif opcion == "1":
            buscar_por_id(clientes)
        elif opcion == "2":
            buscar_por_dni(clientes)
        elif opcion == "3":
            buscar_por_nombre(clientes)
        else:
            print("Opcion invalida.")

# Busca un cliente por su ID numerico.
def buscar_por_id(clientes):
    # Solicita el ID y muestra la ficha del cliente si se encuentra.
    id = input("Ingrese el ID del cliente: ").strip()
    if not validar_id(id):
        print("ID invalido. Debe ser numerico.")
        return
    indice = buscar_indice_por_id(clientes, int(id))
    if indice == -1:
        print("No se encontro un cliente con ese ID.")
        return
    mostrar_detalle_cliente(int(id))

# Busca un cliente por su DNI.
def buscar_por_dni(clientes):
    # Solicita el DNI y muestra la ficha del cliente si se encuentra.
    dni = input("Ingrese el DNI (8 digitos): ").strip()
    if not validar_dni(dni):
        print("DNI invalido. Debe tener exactamente 8 digitos.")
        return
    indice = buscar_indice_por_dni(clientes, dni)
    if indice == -1:
        print("No se encontro un cliente con ese DNI.")
        return
    mostrar_detalle_cliente(clientes[indice]["id"])

# Busca un cliente por su nombre completo.
def buscar_por_nombre(clientes):
    # Solicita el nombre y muestra la ficha del cliente si se encuentra.
    nombre_buscado = input("Ingrese el nombre completo a buscar: ").strip().lower()
    if not nombre_buscado:
        print("Debe ingresar un nombre.")
        return

    for cliente in clientes:
        nombre_cliente = cliente.get("nombre", "").lower()
        if nombre_cliente == nombre_buscado:
            mostrar_detalle_cliente(cliente["id"])
            return

    print("No se encontro un cliente con ese nombre.")
