# importa las funciones necesarias de otros modulos.
from validaciones_menu import ingresar_numero
from autenticacion import autenticar_usuario
from Paquetes_Pack.Menu_Paquetes import menu_paquetes
from Reservas_Pack.Menu_Reservas import menu_reservas
from Clientes_Pack.Menu_Clientes import menu_clientes
# funcion principal que maneja el flujo del programa.
def main():
    # Autenticacion de usuario
    if not autenticar_usuario(): 
        print("No se pudo iniciar sesion. Saliendo...")
        return
    # Menu principal
    while True:    
        print("\n\n=== MENU PRINCIPAL ===")
        print("1. Paquetes")
        print("2. Reservas")
        print("3. Clientes")
        print("0. Salir") 
        # Solicitar opcion al usuario y validar la entrada
        opcion = ingresar_numero("Ingrese opcion: ",0,3)
        # Redirigir a la seccion correspondiente segun la opcion elegida
        if opcion == 1:
            menu_paquetes() 
        elif opcion == 2:
            menu_reservas()
        elif opcion == 3:
            menu_clientes()
        elif opcion == 0:
            print("\nSaliendo del programa...")
            print("Hasta luego!")
            break
# Ejecuta el menu principal cuando se arranca este archivo.
main()
