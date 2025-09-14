from Clientes_Pack.lista_clientes import clientes
def agregar_cliente():
    print("\n=== AGREGAR CLIENTE ===")
    id_cliente = max([c[0] for c in clientes]) + 1
 
    # Validar ID duplicado
    for c in clientes:
        if c[0] == id_cliente:
            print("❌ Ya existe un cliente con ese ID.")
            return

    nombre = input("Ingrese el nombre del cliente: ")

    # Validar que el nombre no este vacio
    if nombre.strip() == "":
        print("❌ El nombre no puede estar vacío.")
        return

    # Ingreso de DNI y validacion
    dni = input("Ingrese el DNI del cliente (solo números): ")
    if not dni.isdigit():
        print("❌ El DNI debe contener solo números.")
        return
    if len(dni) != 8:
        print("❌ El DNI debe tener exactamente 8 dígitos.")
        return

    # Validar DNI duplicado
    for c in clientes:
        if c[2] == dni:
            print("❌ Ya existe un cliente con ese DNI.")
            return

    # Ingreso de Email y validacion
    email = input("Ingrese el Email del cliente: ")
    if email.strip() == "":
        print("❌ El email no puede estar vacío.")
        return

    clientes.append([id_cliente, nombre, dni, email, "Activo"])
    print("✅ Cliente agregado con éxito.")
 