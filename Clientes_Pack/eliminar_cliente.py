from Clientes_Pack.lista_clientes import clientes
def eliminar_cliente():
    print("\n=== ELIMINAR CLIENTE ===")
    id_cliente = input("Ingrese el ID del cliente a eliminar (0 para salir): ")
    if id_cliente == "0":
        print("Saliendo sin eliminar ningún cliente.")
        return

    if not id_cliente.isdigit():
        print("❌ El ID debe ser un número.")
        return
    
    id_cliente = int(id_cliente)

    cliente_encontrado = False
    for c in clientes:
        if c[0] == id_cliente:
            c[4] = "inactivo"  # marcamos como inactivo
            print("✅ Cliente marcado como inactivo.")
            cliente_encontrado = True
            break

    if not cliente_encontrado:
        print("❌ Cliente no encontrado.")
