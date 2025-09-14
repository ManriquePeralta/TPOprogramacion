from Clientes_Pack.mostrar_cliente import mostrar_clientes
from Clientes_Pack.agregar_cliente import agregar_cliente
from Clientes_Pack.modificar_cliente import modificar_cliente
from Clientes_Pack.eliminar_cliente import eliminar_cliente
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
            mostrar_clientes()
        elif op == "2":
            agregar_cliente()
        elif op == "3":
            modificar_cliente()
        elif op == "4":
            eliminar_cliente()
        elif op == "0":
            return
        else:
            print("❌ Opción inválida.")

