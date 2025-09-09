import Clientes_Pack
def menu_clientes():
    op = ""
    while op != "0":
        print("\n=== MENÚ CLIENTES ===")
        print("1. Mostrar clientes")
        print("2. Agregar cliente")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("0. Volver")
        op = input("Opción: ")
        if op == "1":
            Clientes_Pack.mostrar_clientes()
        elif op == "2":
            Clientes_Pack.agregar_cliente()
        elif op == "3":
            Clientes_Pack.modificar_cliente()
        elif op == "4":
            Clientes_Pack.eliminar_cliente()
        elif op == "0":
            return
        else:
            print("❌ Opción inválida.")

