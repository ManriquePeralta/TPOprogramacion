from Clientes_Pack.lista_clientes import clientes
def modificar_cliente():
    print("\n=== MODIFICAR CLIENTE ===")
    id_cliente = input("Ingrese el ID del cliente a modificar: ")

    # Validación: que el ID sea un número
    if not id_cliente.isdigit():
        print("❌ El ID debe ser un número.")
        return
    
    id_cliente = int(id_cliente)
    cliente_encontrado = False

    for c in clientes:
        if c[0] == id_cliente:
            cliente_encontrado = True
            print(f"Cliente encontrado: {c[1]}")

            # Nuevo nombre
            nuevo_nombre = input("Ingrese el nuevo nombre completo (dejar en blanco para no cambiar): ")
            if nuevo_nombre != "":
                c[1] = nuevo_nombre

            # Nuevo DNI
            nuevo_dni = input("Ingrese el nuevo DNI (dejar en blanco para no cambiar): ")
            if nuevo_dni != "":
                if not nuevo_dni.isdigit():
                    print("❌ El DNI debe contener solo números.")
                    return
                # Validar que no esté duplicado en otro cliente
                for otro in clientes:
                    if otro[2] == nuevo_dni and otro[0] != id_cliente:
                        print("❌ Ese DNI ya pertenece a otro cliente.")
                        return
                c[2] = nuevo_dni

            # Nuevo Email
            nuevo_email = input("Ingrese el nuevo email (dejar en blanco para no cambiar): ")
            if nuevo_email != "":
                c[3] = nuevo_email

            print(f"✅ Cliente ID {id_cliente} modificado con éxito.")
            break

    if not cliente_encontrado:
        print(f"❌ No se encontró un cliente con ID {id_cliente}.")
