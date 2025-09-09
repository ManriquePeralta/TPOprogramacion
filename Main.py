from Paquetes_Pack.Menu_Paquetes import menu_paquetes
from Reservas_Pack.Menu_Reservas import menu_reservas
from Clientes_Pack.Menu_Clientes import menu_clientes

def main():
    op = ""
    while op != "0":
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Paquetes")
        print("2. Reservas")
        print("3. Clientes")
        print("0. Salir")
        op = input("Opción: ")
        if op == "1":
            menu_paquetes()
        elif op == "2":
            menu_reservas()
        elif op == "3":
            menu_clientes()
        elif op == "0":
            print("👋 ¡Hasta luego!")
        else:
            print("❌ Opción inválida.")

main()